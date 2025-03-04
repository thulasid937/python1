
'''
from tkinter import*

top=Tk()
top.geometry("400x250")

def ss():
        print("How are you")

btn5=Button(top,text="OK",width=10,activebackground="yellow",
            font=("Times New Roman",20,"bold"),foreground="white",
            background="#26B3E8",command=ss)
btn5.place(x=0,y=0)

btn6=Button(top,text="BACK",width=10,
            activebackground="purple",
            font=("Times New Roman",20,"bold"),foreground="white",
            background="RED",command=top.destroy)

btn6.place(x=200,y=0)

top.mainloop()
'''
'''
from tkinter import*
top=Tk()
top.geometry("400x250")
name=Label(top,text="Name",font=("Times New Roman",20,"bold"))
name.place(x=30,y=50)

email=Label(top,text="Email")
email.place(x=30,y=100)

password=Label(top,text="Password")
password.place(x=30,y=150)

n1=Entry(top,text=("Times New Roman",15,"bold"))
n1.place(x=120,y=50)

n2=Entry(top)
n2.place(x=120,y=100)

n3=Entry(top)
n3.place(x=120,y=150)

top.mainloop()
'''
'''
from tkinter import*
from tkinter import messagebox
top=Tk()
top.geometry("400x250")
def fun():
        messagebox.showinfo("Hello","ALL THE BEST")
        
def fun1():
        messagebox.showerror("Hello","Something wrong")

b1=Button(top,text="Submit",command=fun)
b1.pack()
b2=Button(top,text="Cancel",command=fun1)
b2.pack()
top.mainloop()
'''





