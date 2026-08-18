# cd Simple-Calculator
# cd Python_project
# cd GUI_project

# step1 : importing
from tkinter import *
from tkinter import ttk
from tkinter import font
# step2 : gui intraction
window=Tk()
window.title("GUI Calculator")
window.geometry('5000x5000')

# step3 : adding input 

# ===================================================================================================
# ENTRY BOX
custom_font=font.Font(family="Times New Roman",size=15,slant="italic",weight="bold")
l=Label(text="Mini Calculator",
        font=("Times New Roman",25,"italic","bold"),
        pady=20,
        fg="white",
        bg="maroon")
l.pack(fill='x',side=TOP)

e=Entry(window,width=56,borderwidth=5,
        font=custom_font,
        fg="green",
        justify="center")
e.focus()
e.pack(side=TOP,pady=90)
# e.place(x=10,y=60)

# ===================================================================================================
# BUTTON

def click(num):
    result=e.get()
    e.delete(0,END)
    ei=e.insert(0,str(result) + str(num))
#     print(ei)
#     print(result)
b=Button(text="1",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(1))
b.place(x=555,y=280)

b=Button(text="2",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(2))
b.place(x=660,y=280)

b=Button(text="3",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(3))
b.place(x=765,y=280)

b=Button(text="4",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(4))
b.place(x=870,y=280)

b=Button(text="5",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(5))
b.place(x=555,y=338)

b=Button(text="6",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(6))
b.place(x=660,y=338)

b=Button(text="7",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(7))
b.place(x=765,y=338)

b=Button(text="8",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(8))
b.place(x=870,y=338)

b=Button(text="9",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(9))
b.place(x=555,y=396)

b=Button(text="0",font=custom_font,padx=40,pady=10,background="pink",command=lambda:click(0))
b.place(x=660,y=396)

# ==================================================================================================
# OPERATORS


def add():
    global n
    n=e.get()
    global math
    math = "addition"
    e.delete(0,END)

b=Button(text="+",font=custom_font,padx=39,pady=10,background="pink",command=add)
b.place(x=555.5,y=454)

def sub():
    global n
    n=e.get()
    global math
    math="subtraction"
    e.delete(0,END)

b=Button(text="-",font=custom_font,padx=42,pady=10,background="pink",command=sub)
b.place(x=660,y=454)

def mul():
    global n
    n=e.get()
    global math
    math="multiplication"
    e.delete(0,END)

b=Button(text="*",font=custom_font,padx=39.5,pady=10,background="pink",command=mul)
b.place(x=766,y=454)

def div():
    global n
    n=e.get()
    global math
    math="division"
    e.delete(0,END)

b=Button(text="/",font=custom_font,padx=40.5,pady=10,background="pink",command=div)
b.place(x=871,y=454)

def equal():
#     global math
    
    m=e.get()
    e.delete(0,END)

    if math == "addition":
        k=e.insert(0,int(n)+int(m))

        print(n,"+",m,"=",int(n)+int(m))
    elif math == "subtraction":
        k=e.insert(0,int(n)-int(m))
        
        print(n,"-",m,"=",int(n)-int(m))
    elif math=="multiplication":
        print(n,"*",m)
        k=e.insert(0,int(n)*int(m))
        
        print(n,"*",m,"=",int(n)*int(m))
    elif math=="division":
        print(n,"/",m)
        k=e.insert(0,int(n)/int(m))

        print(n,"/",m,"=",int(n)/int(m))
b=Button(text="=",font=custom_font,padx=40,pady=10,background="pink",command=equal)
b.place(x=765,y=396)

def clear():
    e.delete(0,END)

b=Button(text="clear",font=("Times New Roman",14,"italic","bold"),padx=25,pady=10,background="pink",command=clear)
b.place(x=871,y=396)

l=Text(font=("Times New Roman",14,"italic","bold"),height=3,width=35)
# Label(text="Right now history button only shows current value....",font=custom_font)
l.place(x=590,y=600)

l.insert("1.0"," Right  now   history   button   doesn't  show  anything....")
def history():
    i=e.get()
    # print(i)
        # if math == "addition":
        # ^^^^
        # NameError: name 'math' is not defined. Did you forget to import 'math'?
    # l.config(text=i)
bh=Button(font=custom_font,text="History",width=35,command=history)
bh.place(x=570,y=530)
l["state"]="disabled"
# ===================================================================================================
# step 4 : mainloop
window.mainloop()