from tkinter import *
import math
class MainWindow:
    def __init__(self):     
        self.root = Tk()
        textList=["hello","folks","Jan"]
        self.root.title("account")
        self.invest_amnt = DoubleVar()
        self.intrest_rate = DoubleVar()
        self.years = DoubleVar()
        Label(
        self.root,
        text="investment ammount"
        ).grid(row=0, column=0)
        Entry(
        self.root,
        text=self.invest_amnt
        ).grid(row=0, column=1)
        Label(
        self.root,
        text="years"
        ).grid(row=1, column=0)
        Entry(
        self.root,
        text=self.years
        ).grid(row=1, column=1)
        Label(
        self.root,
        text="annual interest rate"
        ).grid(row=2, column=0)
        Entry(
        self.root,
        text=self.intrest_rate
        ).grid(row=2, column=1)
        Label(
        self.root,
        text="future investment"
        ).grid(row=3, column=0)
        Button(
        self.root,
        text="calculate",
        fg="blue",
        command=self.onclick
        ).grid(row=4, column=1)
        j=5
        for t in textList:
            Label(
            self.root,
            text=t
            ).grid(row=j, column=0)
            j+=1
        self.root.mainloop()
                
    def onclick(self):
        ans = self.invest_amnt.get() * (1 + self.intrest_rate.get()) ** (self.years.get() * 12)
        Label(
        self.root,
        text=str(ans)
        ).grid(row=3, column=1)
MainWindow()
