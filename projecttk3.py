import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font
import sqlite3

root=tkinter.Tk()
root.title("login form")
root.geometry("400x300")
root.resizable(False,False)
root.configure(bg="#413839")

username=Label(root,text="username",bg="#413839",fg="#FFFFFF")
username.grid(row=0,column=0)

username_Entry=Entry(root,width=10)
username_Entry.grid(row=0,column=1)

password=Label(root,text="password",bg="#413839",fg="#FFFFFF")
password.grid(row=1,column=0)

password_Entry=Entry(root,width=10,show="*")
password_Entry.grid(row=1,column=1)

confirm_password=Label(root,text="confirm password",bg="#413839",fg="#FFFFFF")
confirm_password.grid(row=2,column=0)

c_Entry=Entry(root,width=10,show="*")
c_Entry.grid(row=2,column=1)

def confirm():
    c=password_Entry.get()
    d=c_Entry.get()
    b=username_Entry.get()

    
    connection=sqlite3.connect("loginform.db")
    cursor=connection.cursor()
    
    cursor.execute("create table if not exists loginform (username text,password text)")


        
    
    if(c==d and c!="" and b!="" ):
        cursor.execute("insert into loginform values(:username,:password)",{'username':username_Entry.get(),'password':password_Entry.get(),})
        username_Entry.delete(0,END)
        password_Entry.delete(0,END)
        c_Entry.delete(0,END)
    
        tkinter.messagebox.showinfo("login form","password fixed")
    elif(c==""):
        tkinter.messagebox.showinfo("login form","password is not entered")
    elif(b==""):
        tkinter.messagebox.showinfo("login form","username is not entered")
    else:
        tkinter.messagebox.showinfo("login form","password error")
    connection.commit()
    connection.close()


confirm=Button(root,text="confirm",width=10,command=confirm,bg="#00BFFF",fg="#333333")
confirm.grid(row=3,column=1)



