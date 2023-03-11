from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import messagebox
from tkinter import *


a = CurrencyConverter()
root = tk.Tk()
root.title("Currency Converter")
root.config(bg="#4863A0")
root.geometry("500x350")
img1 = PhotoImage(file="coins.png")
img2 = PhotoImage(file="exchange.png")
photo_label = tk.Label(root, bg="#4863A0", image=img1, height=70, width=90)
photo_label.place(x=5, y=0)
root.iconphoto(False, img2)


def submit():
    try:
        amount = int(et1.get())
        currency_1 = et2.get().upper()
        currency_2 = et3.get().upper()
        data = a.convert(amount, currency_1, currency_2)
        lb5 = tk.Label(root, text= data,fg="#FFFFFF", bg="#4863A0", font="Times 25 bold").place(x=60, y=290)
    except:
        messagebox.showerror(title="ERROR!", message="Enter a valid number or a valid currency!!!")

def reset():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)


#Label 1
lb1 = tk.Label(root, text="CURRENCY CONVERTER", fg="#FFFFFF", bg="#4863A0", font="Times 20 bold").place(x=80, y=20)

#Label 2
lb2 = tk.Label(root, text="Enter amount: ", fg="#FFFFFF", bg="#4863A0", font="Times 18 bold").place(x=50, y=80)
et1 = tk.Entry(root)
et1.place(x=300, y=90)

#Label 3
lb3 = tk.Label(root, text="From: ", fg="#FFFFFF", bg="#4863A0", font="Times 18 bold").place(x=50, y=130)
et2 = tk.Entry(root)
et2.place(x=300, y=140)

#Label 4
lb4 = tk.Label(root, text="To: ", fg="#FFFFFF", bg="#4863A0", font="Times 18 bold").place(x=50, y=180)
et3 = tk.Entry(root)
et3.place(x=300, y=190)

#Button 1
bt1 = tk.Button(root, text="CONVERT",fg="#FFFFFF", bg="#C19A6B", font="Times 15 bold", command= submit).place(x=60, y=240)

#Button 2
bt2 = tk.Button(root, text="RESET",fg="#FFFFFF", bg="#C19A6B", font="Times 15 bold", command= reset).place(x=300, y=240)



root.mainloop()





