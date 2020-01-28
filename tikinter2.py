from tkinter import *
from PIL import Image,ImageTk
window=Tk()
window.geometry('500x500')
window.title('Registration Form')

# root=Tk()
# root.geometry('500x500')
# root.title('Registration Form2')

width = 100
height = 100
img=Image.open("D:/Python/tikinter/clipart.jpg")
img = img.resize((width,height),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(img)

lab=Label(image=photo)
lab.pack()

# img=Image.open("D:/Python/tikinter/shtk.jpg")
# photo1=ImageTk.PhotoImage(img)
# lab=Label(image=photo1)
# lab.pack()

fn1=StringVar()
fn2=StringVar()
fn3=StringVar()
var=StringVar()

def printt():
    first=fn1.get()
    sec=fn2.get()
    index=fn3.get()
    var1=var.get()
    print(f"Your Fullname is :{first} {sec}")
    print(f"Your Index is :{index}")
    print(f"Your Country is :{var1}")

def end():
    exit()

lable1=Label(window,text="Registration Form",relief="solid",width=20,font=('arial',19,'bold'))
lable1.place(x=90,y=110)


lable2=Label(window,text="Frist Name:",font=('arial',10,'bold'))
lable2.place(x=90,y=160)
entry1=Entry(window,textvar=fn1)
entry1.place(x=200,y=160)

lable3=Label(window,text="Last Name:",font=('arial',10,'bold'))
lable3.place(x=90,y=200)
entry1=Entry(window,textvar=fn2)
entry1.place(x=200,y=200)

lable4=Label(window,text="Index:",font=('arial',10,'bold'))
lable4.place(x=90,y=240)
entry1=Entry(window,textvar=fn3)
entry1.place(x=200,y=240)

lable4=Label(window,text="Country:",font=('arial',10,'bold'))
lable4.place(x=90,y=280)



list1=['Sri Lanka','India','USA','Canada','German']
droplist=OptionMenu(window,var,*list1)
var.set('Select country')
droplist.config(width=15)
droplist.place(x=200,y=280)




b1=Button(window,text='login',relief='solid',width=12,font=('aril',10),command=printt)
b1.place(x=90,y=350)
b2=Button(window,text='Quit',relief='solid',width=12,font=('aril',10),command=end)
b2.place(x=300,y=350)
window.mainloop()