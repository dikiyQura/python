from tkinter import *
from tkinter import Tk
import pyttsx3
engine = pyttsx3.init()


def clicked():
    res ="{}".format(txt.get())
    a=res
    if res== 'one':
        b = ('один')
    elif res== 'two':
        b = ('два')
    elif res== 'three':
        b = ('Уч')
    elif res== 'four':
        b = ('четыре')
    else:
        b = ('Данное слово не существует')
    lbl1.configure(text=b)
def say():

    res1 ="{}".format(txt.get())
    if res1== 'one':
        b1 = ('один')
    elif res1== 'two':
        b1 = ('два')
    elif res1== 'three':
        b1 = ('три')
    elif res1== 'four':
        b1 = ('четыре')
    else:
        b1 = ('Данное слово не существует')
    engine.say(b1)
    engine.runAndWait()




window = Tk()
window.title("переводчик")
window.geometry('400x250')
lbl = Label(window, text='ПЕРЕВОДЧИК' , )
lbl.grid(column=11, row=0)

txt = Entry(window, width=10)
txt.grid(column=4, row=4)

btn = Button(window, text='>', bg="black", fg="white", command=clicked )
btn.grid(column=10, row=4)

btn = Button(window, text='🔊', command=say)
btn.grid(column=11,row=2)
lbl1 = Label(window, width="22")
lbl1.grid(column=11, row=4)

window.mainloop()
