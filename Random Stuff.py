from tkinter import *
import random
root=Tk()
root.title("Picnic Bag")
root.geometry("400x400")
root.configure(background="blue")

title=Label(root,text="Picnic Bag", font=('Arial',15), background="Lightblue")
list1=["Gems","KitKat","Watch","Tshirt","Pencil"]
label2=Label(root,text="Listed Items: "+str(list1),background="lightgreen")
label1=Label(root,text="")

def luckyfriend():
    random_number=random.randint(0,4)
    luckyFriend=list1[random_number]
    label1["text"]="Item to Carry: "+luckyFriend

button1=Button(root,text="Show Item To Carry.", command=luckyfriend, background="yellow")
title.place(relx=0.5, rely=0.3, anchor=CENTER)
label2.place(relx=0.5, rely=0.4, anchor=CENTER)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()