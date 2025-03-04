##--------------------Window Frame--------------------------------
##from tkinter import*
##top=Tk() #Application creati
##top.title("GUI WINDOW") #title
##top.geometry("750x400")  #size 
##top.config(bg="#1b88dd")  #background color(#hexadecimal)
##
##top.mainloop() #to run the events






##
##
##Tkinter is a Python library that can be used to construct basic graphical
##user interface (GUI) applications.In Python,
##it is the most widely used module for GUI applications.
##
###----- DESIGN FOR BUTTON
##from tkinter import*
##top=Tk()
##top.geometry("400x250")
##
##def ss():
##    print('How are you')
##    
##btn5=Button(top,text="OK",width=10,activebackground="yellow",
##            font=("Times New Roman",20,"bold"),foreground="white",    
##            background="#26B3E8",command=ss)
##btn5.place(x=0,y=0)
##
##btn6=Button(top,text="BACK",width=10,
##            activebackground="yellow",       
##            font=("Times New Roman",20,"bold"),foreground="white",        
##            background="RED",command=top.destroy)
##
##btn6.place(x=200,y=0)
##
##top.mainloop()















##-----------------Label & Entry Box------------------
####
##from tkinter import*
##top=Tk()
##top.geometry("400x250")
##name=Label(top,text="Name",font=("Times New Roman",20,"bold"))
##name.place(x=30,y=50)
##
##email=Label(top,text="Email")
##email.place(x=30,y=100)
##
##password=Label(top,text="Password")
##password.place(x=30,y=150)
##
##n1=Entry(top,font=("Times New Roman",15,"bold"))
##n1.place(x=120,y=50)
##
##n2=Entry(top)
##n2.place(x=120,y=100)
##
##n3=Entry(top)
##n3.place(x=120,y=150)
##
##top.mainloop()

####----------------------Messagebox--------------------------
##from tkinter import*
##from tkinter import messagebox
##top=Tk()
##top.geometry("400x400")
##def fun():
##    messagebox.showinfo("Hello","All The BEst")
##    
##def fun1():
##    messagebox.showerror("Hello","Something Wrong")
##    
##b1=Button(top,text="Submit",command=fun)
##b1.pack()
##b2=Button(top,text="Cancel",command=fun1)
##b2.pack()
##top.mainloop()

 



#---------create a frame inside the main page--------


##from tkinter import*
##from tkinter import messagebox
##top=Tk()
##top.title("LOGIN SAMPLE") 
##top.config(bg='lightblue')
##top.geometry("400x250")
##def msg():
##    messagebox.showinfo("THird Page","Welcome")
##    
##def nxt():
##    f1=Frame(top,height=1250,width=1200,bg='pink')
##    f1.pack()
##
##    btn1=Button(f1,text="Next",width=10,
##            
##            font=("Vegan Style",10,"bold"),foreground="white",
##            
##            background="lightblue",command=msg).place(x=25,y=125)
##
##    btn2=Button(f1,text="Back",width=10,
##            
##            font=("Times New Roman",10,"bold"),foreground="white",
##            
##            background="lightblue",command=f1.destroy).place(x=150,y=125)
##    
####first page
##name=Label(top,text="Name").place(x=30,y=50)
##
##password=Label(top,text="Password").place(x=30,y=100)
##
##n1=Entry(top)
##n1.place(x=100,y=50)
##
##n2=Entry(top)
##n2.place(x=100,y=100)
##
##btn5=Button(top,text="OK",width=10,activebackground="yellow",
##            
##            font=("Times New Roman",10,"bold"),foreground="white",
##            
##            background="green",command=nxt).place(x=25,y=125)
##
##top.mainloop()


#-------------TO PLACE THE IMAGE IN TKINTER-----------------

from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk #pip install pillow
top=Tk()

top.title("PLAYER PROFILE") 
top.config(bg='lightblue')
top.geometry("1000x1000")
top.resizable(True,True)

#Images Place
img=Image.open('Dhoni.png')
img=img.resize((1000,1000))
img2=ImageTk.PhotoImage(img)
imglabel=Label(top,image=img2)
imglabel.image=img2
imglabel.place(x=0,y=0)

name=Label(top,text="M S  D H O N I",
           font=('Algerian', 40, 'bold'),bg="#DBC400",fg="black")
name.place(x=0,y=10)

#label
role = Label(top, text=" ROLE", font=("Calibri", 20,"bold"),
             bg="#DBC400", fg="black")
role.place(x=0, y=150)

bat = Label(top, text=" BATS", font=("Calibri", 20,"bold"),
            bg="#DBC400", fg="black")
bat.place(x=0, y=220)

bowl = Label(top, text=" BOWLS", font=("Calibri", 20,"bold"),
             bg="#DBC400", fg="black")
bowl.place(x=0, y=290)

catch = Label(top, text=" CATCH", font=("Calibri", 20,"bold"), bg="#DBC400", fg="black")
catch.place(x=0, y=360)

role = Label(top, text=" WICKET KEEPING", font=("Calibri", 20,"bold"), bg="#042B3A", fg="white")
role.place(x=130, y=150)
## 
bat = Label(top, text=" RIGHT HAND", font=("Calibri", 20,"bold"), bg="#042B3A", fg="white")
bat.place(x=130, y=220)
##
bowl = Label(top, text=" MEDIUM FAST", font=("Calibri", 20,"bold"), bg="#042B3A", fg="white")
bowl.place(x=130, y=290)
##
catch = Label(top, text=" 500", font=("Calibri", 20,"bold"), bg="#042B3A", fg="white")
catch.place(x=130, y=360)


top.mainloop()
  ##################################################################




##Treeview

##
##import tkinter as tk
##from tkinter import ttk
##
##def open_treeview():
##    for widget in root.winfo_children():
##        widget.destroy()
##    
##    frame = tk.Frame(root,height=1200,width=700)
##    frame.pack(fill=tk.BOTH, expand=True)
##    
##    tree = ttk.Treeview(frame)
##    tree.pack(fill=tk.BOTH, expand=True)
##    
##    # Define columns
##    tree["columns"] = ("Mobile Number", "Email", "Age")
##    
##    tree.column("#0", width=150, minwidth=150)
##    tree.column("Mobile Number", width=120, minwidth=120)
##    tree.column("Email", width=150, minwidth=150)
##    tree.column("Age", width=50, minwidth=50)
##    
##    # Define headings
##    tree.heading("#0", text="Name", anchor=tk.W)
##    tree.heading("Mobile Number", text="Mobile Number", anchor=tk.W)
##    tree.heading("Email", text="Email", anchor=tk.W)
##    tree.heading("Age", text="Age", anchor=tk.W)
##    
##    # Add data
##    tree.insert("", "end", text="John Doe", values=("9876543210", "john@example.com", "30"))
##    tree.insert("", "end", text="Jane Smith", values=("8765432109", "jane@example.com", "28"))
##    tree.insert("", "end", text="Alice Brown", values=("7654321098", "alice@example.com", "25"))
##    
##
##
##
##    
##
##root = tk.Tk()
##root.title("Main Window")
##root.geometry("700x500")
##btn = tk.Button(root, text="Open Tree View", command=open_treeview)
##btn.pack(pady=20)
##
##root.mainloop()












