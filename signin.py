
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


# Functionality
def forget_password():
    def change_password():
        if user_entry.get() == '' or newpassword_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required', parent=window)

        elif newpassword_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not Matching',
                                 parent=window)

        else:
            con = pymysql.connect(host='localhost', user='root', password='Achal@453', database='userdatadb')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query, (newpassword_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset,please login with new password', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change Password')
    bgPic = ImageTk.PhotoImage(file='bg.jpg')
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid()
    heading_label = Label(window, text='RESET PASSWORD', font=('arial', '18', 'bold'), bg='white', fg='red')
    heading_label.place(x=490, y=50)

    user_Label = Label(window, text='Username', font=('arial', 12), bg='white', fg='firebrick1')
    user_Label.place(x=483, y=100)

    user_entry = Entry(window, width=25, fg='firebrick1', font=('arial', 11, 'bold'), bd=0)
    user_entry.place(x=485, y=125)

    Frame(window, width=250, height=2, bg='red').place(x=485, y=145)

    newpassword_Label = Label(window, text='New Password', font=('arial', 12), bg='white', fg='firebrick1')
    newpassword_Label.place(x=483, y=180)

    newpassword_entry = Entry(window, width=25, fg='firebrick1', font=('arial', 11, 'bold'), bd=0)
    newpassword_entry.place(x=485, y=210)

    Frame(window, width=250, height=2, bg='red').place(x=485, y=230)

    confirmpass_Label = Label(window, text='Confirm Password', font=('arial', 12), bg='white', fg='firebrick1')
    confirmpass_Label.place(x=480, y=260)

    confirmpass_entry = Entry(window, width=25, fg='firebrick1', font=('arial', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=485, y=290)

    Frame(window, width=250, height=2, bg='red').place(x=485, y=310)

    submitButton = Button(window, text='Submit', bd=0, bg='red', fg='white', font=('Open Sans', '16', 'bold'),
                          width=19, cursor='hand2', activebackground='red', activeforeground='white',
                          command=change_password)
    submitButton.place(x=482, y=360)

    window.mainloop()


def signup_page():
    login_window.destroy()
    import signup


def user_enter(self):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(self):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)



def login_user():
    if (usernameEntry.get() == ' ' or passwordEntry.get()== ' '):
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Achal@453', database='userdatadb')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue,Please Try Again')
            return

        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or Password')

        else:

            query='insert into data(username,password) values(%s,%s)'
            mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Login is Successful')
            


# GUI part
login_window = Tk()
login_window.geometry('800x660+40+50')
login_window.resizable(0, 0)
login_window.title('Login Page')
bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.grid(row=0, column=0)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft yahei UI Light', 23, 'bold'), bg='White',
                fg='firebrick1')
heading.place(x=505, y=70)

# user entry
usernameEntry = Entry(login_window, width=25, font=('Microsoft yahei UI Light', 10, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=480, y=150)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=480, y=170)

# password entry
passwordEntry = Entry(login_window, width=25, font=('Microsoft yahei UI Light', 10, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=480, y=210)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=480, y=230)

# eye button
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                   command=hide)
eyeButton.place(x=700, y=203)

forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2'
                      , font=('Microsoft yahei UI Light', 9, 'bold'), fg='firebrick1', activeforeground='firebrick1',
                      command=forget_password)
forgetButton.place(x=620, y=235)

# Login button
loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'),
                     fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1',
                     cursor='hand2', bd=0, width=18, command=login_user)
loginButton.place(x=478, y=290)

orLabel = Label(login_window, text='--------------OR----------------', font=('Open Sans', 16), fg='firebrick1',
                bg='white')
orLabel.place(x=475, y=340)

# LOGOS
facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=520, y=380)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=570, y=380)

twitter_logo = PhotoImage(file='twitter.png')
twLabel = Label(login_window, image=twitter_logo, bg='white')
twLabel.place(x=620, y=380)

signupLabel = Label(login_window, text='Dont have an account?', font=('Open Sans', 10, 'bold'), fg='firebrick1',
                    bg='white')
signupLabel.place(x=475, y=420)

newaccountButton = Button(login_window, text='Create new one', font=('Open Sans', 8, 'bold underline'),
                          fg='dark blue', bg='white', activeforeground='dark blue', activebackground='white',
                          cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=625, y=420)

login_window.mainloop()
