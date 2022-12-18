import tkinter
from tkinter import *
from tkinter import messagebox


root=tkinter.Tk()
root.title("Mark Calculator")
root.geometry("400x200")
root.resizable(False,False)

def Average():
    a=int(English_Entry.get())
    b=int(Tamil_Entry.get())
    c=int(Math_Entry.get())
    d=int(science_Entry.get())
    e=int(social_Entry.get())
    f=(a+b+c+d+e)/5
    tkinter.messagebox.showinfo("Average",f)
    
    
Name=Label(root,text="STUDENT NAME")
Name.grid(row=0,column=0)

Name_Entry=Entry(root,width=10)
Name_Entry.grid(row=0,column=1)

English=Label(root,text="ENGLISH")
English.grid(row=1,column=0)

English_Entry=Entry(root,width=10)
English_Entry.grid(row=1,column=1)

Tamil=Label(root,text="TAMIL")
Tamil.grid(row=2,column=0)

Tamil_Entry=Entry(root,width=10)
Tamil_Entry.grid(row=2,column=1)

Math=Label(root,text="MATH")
Math.grid(row=3,column=0)

Math_Entry=Entry(root,width=10)
Math_Entry.grid(row=3,column=1)

Science=Label(root,text="SCIENCE")
Science.grid(row=4,column=0)

science_Entry=Entry(root,width=10)
science_Entry.grid(row=4,column=1)

Social=Label(root,text="SOCIAL")
Social.grid(row=5,column=0)

social_Entry=Entry(root,width=10)
social_Entry.grid(row=5,column=1)

    
Validate=Button(root,text="Validate",width=10,command=Average)
Validate.grid(row=7,column=0)

