import tkinter as tk
from tkinter import *
import random
import time

with open('list1.txt', 'r') as f:
    a = f.readlines()

text = ""
for i in range(0,5):
    word = random.choice(a)
    word = word[:-1]
    if i == 4:
        text += word+"."
    elif i == 0:
        text += word.capitalize() + " "
    else:
        text += word+" "

count = 0
count1 = 1
a = 0
b = 0
timercount = True
start_time1 = 0
def spell_check(vari, indx, mode):
    global a,b,count,count1,timercount,start_time1
    if timercount:
        start_time1 = time.time()
        timercount = False
    if len(var.get()) - count == -1:
        count -= 1
        count1 -= 1
        text_label.tag_add(f"start{count}", f"1.{count}", f"1.{count+1}")
        text_label.tag_config(f"start{count}", foreground="black")
    else:
        if var.get()[-1] == text[count] and len(var.get()) == count1:
            text_label.tag_add(f"start{count}", f"1.{count}", f"1.{count+1}")
            text_label.tag_config(f"start{count}", foreground="green")
        elif var.get()[-1] != text[count] or len(var.get()) != count1:
            text_label.tag_add(f"start{count}", f"1.{count}", f"1.{count+1}")
            text_label.tag_config(f"start{count}", foreground="red")
        count += 1
        count1 += 1
    if var.get()[-1] == "." and len(var.get()) == len(text):
        end()
lps = 1
def end():
    global lps
    lps = len(text)/(time.time()-start_time1)
    window.destroy()
    root = Tk()
    root.geometry('400x200')
    label = Label(root, text=f"your total speed was : {round(lps,2)} letters per second")
    label.pack()
    root.mainloop()

window = Tk()
window.title("Type Racer")
window.geometry('700x600')

text_label = Text(window)
text_label.pack()
text_label.insert(INSERT,text)

var = StringVar()
var.trace_add("write", spell_check)
Entry(window, textvariable=var).pack(padx=5,pady=5)
window.mainloop()
