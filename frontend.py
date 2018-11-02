from tkinter import *
import tkinter as tk 
import math
from PIL import Image, ImageTk

class MainWindow:
    def __init__(self): 
        self.t=None
        self.name=""
        self.carint=""
        self.contact=""
        self.address=""
        
        self.registe_page()
        
    def redirecT(self,old_win):
        old_win.destroy()
        self.dispHeaader()
    def registe_page(self):
        r=0
        t=Tk()
        
        t.configure(background="#a3a5b7")
        t.geometry("1400x800")
        Label(t,
            font=('sans serif', 20 , 'bold'), 
            text="                 Wheels To Go\nNear NMAM Institute of Technology\n   Nitte - 574110, Karkala, Udupi", 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7"
        ).grid(row=r,column=1)
        r+=1

        Label(
            t,
            text="\n\n\n\n",
            fg="#29293d",
            bg="#a3a5b7",
        ).grid(row=r,column=0)

        Label(
            t,
            font=('sans serif', 14 , 'bold'), 
            text="Enter your name :",
            width=30, 
            justify=RIGHT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
        ).grid(row=r,column=0,padx=10,pady=10)

        Entry(
            t,
            font=('sans serif', 14 ), 
            text=self.name, 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7"
        ).grid(row=r,column=1)
        r+=1
        

        Label(
            t,
            font=('sans serif', 14 , 'bold'), 
            text="Car you are interested in : ",
            width=30, 
            justify=RIGHT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
        ).grid(row=r,column=0,padx=10,pady=10)

        Entry(
            t,
            font=('sans serif', 14 ), 
            text=self.carint, 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7"
        ).grid(row=r,column=1)
        r+=1
        
        Label(
            t,
            font=('sans serif', 14 , 'bold'), 
            text="Contact Number : ",
            width=30, 
            justify=RIGHT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
        ).grid(row=r,column=0,padx=10,pady=10)

        Entry(
            t,
            font=('sans serif', 14 ), 
            text=self.contact, 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7"
        ).grid(row=r,column=1)
        r+=1
        
        
        Label(
            t,
            font=('sans serif', 14 , 'bold'), 
            text="Address : ",
            width=30, 
            justify=RIGHT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
        ).grid(row=r,column=0,padx=10,pady=10)

        Entry(
            t,
            font=('sans serif', 14 ), 
            text=self.address, 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7"
        ).grid(row=r,column=1)
        r+=1
        
        print(str(self.name)+"  "+str(self.carint)+"  "+str(self.contact)+"  "+str(self.address))


        
        self.t=t
        
        Button(
            t,
             font=('sans serif', 20 , 'bold'), 
            text="Go to home", 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
            command=self.disp1
       ).grid(row=r,column=0)

        Button(
            t,
             font=('sans serif', 20 , 'bold'), 
            text="About us", 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
            command=self.disp2
       ).grid(row=r,column=1)
        

        Button(
            t,
             font=('sans serif', 20 , 'bold'), 
            text="Exit...", 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
            command=self.disp3
       ).grid(row=r,column=2)
        
        
        
        t.mainloop()
    def disp1(self):
            
        self.t.destroy()
        self.dispHeaader()
    def disp2(self):

        self.t.destroy()
        self.dispinfo()
    def dispinfo(self):
        i=Tk()
        i.configure(background="#a3a5b7")
        txt="                 Wheels To Go\nNear NMAM Institute of Technology\n   Nitte - 574110, Karkala, Udupi"
        
        Label(
            i,
            font=('sans serif', 20 , 'bold'), 
            text=txt, 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
       ).grid(row=0,column=1)
        
        
        icon1 = ImageTk.PhotoImage(Image.open('f.jpg'))
        icon_size1 = Label(i)
        icon_size1.image = icon1
        icon_size1.justify=LEFT
        icon_size1.configure(image=icon1,width=200,height=200)
        icon_size1.grid(row=1,column=0,padx=100,pady=20)
        
        icon2 = ImageTk.PhotoImage(Image.open('f.jpg'))
        icon_size2 = Label(i)
        icon_size2.image = icon2
        icon_size2.justify=LEFT
        icon_size2.configure(image=icon2,width=200,height=200)
        icon_size2.grid(row=1,column=1,padx=20,pady=20)
        

        

        
        Label(
            i,
            font=('sans serif', 10 , 'bold'), 
            text="\n\nName: Prasanna Vittala Moolya\nUSN: 4NM15CS118" , 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
       ).grid(row=2,column=0,padx=20,pady=20)

        Label(
            i,
            font=('sans serif', 10 , 'bold'), 
            text="\n\nName: Tejukumar\nUSN: 4NM16CS403" , 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
       ).grid(row=2,column=1,padx=20,pady=20)




        i.mainloop()

    def disp3(self):
        self.t.destroy()

    def dispHeaader(self):
        self.cars=["Ankitha","Prasanna","Ankitha","Prasanna","Ankitha","Prasanna"]    
        self.root = Tk()
        self.root.configure(background="#a3a5b7")
        self.root.geometry("1400x800")
        self.row=0
        self.title="                 Wheels To Go\nNear NMAM Institute of Technology\n   Nitte - 574110, Karkala, Udupi"
        self.info="\nMaruti Suzuki India Limited, formerly\nknown as Maruti Udyog Limited, is\nan automobile manufacturer in India.\nIt is a 56.21 owned subsidiary\nof the Japanese car and motorcycle manufacturer\nSuzuki  Motor Corporation. As of July\n2018, it had a market share of 53'%'\nof the Indian passenger car market.\n"
        self.bg="#a3a5b7"
        
        
        Label(self.root,
        font=('sans serif', 20 , 'bold'), 
        text=self.title, 
        justify=LEFT,
        bd=1,
        fg="#29293d",
        bg="#a3a5b7"
       ).grid(row=self.row,column=1)
        self.row+=1
        Label(self.root,
        
        width=43,
        font=('sans serif', 12), 
        text=self.info, 
        justify=LEFT,
        bd=1,
        fg="#f2f4f7",
        bg="#465670",
        ).grid(row=self.row,column=0,padx=5,pady=5)
        self.row+=1

        Label(self.root,
        width=43,
        font=('sans serif', 12), 
        text=self.info, 
        justify=LEFT,
        bd=1,
        fg="#f2f4f7",
        bg="#465670",
        ).grid(row=self.row-1,column=1)
        self.row+=1

        Label(self.root,
        width=43,
        font=('sans serif', 12), 
        text=self.info, 
        justify=LEFT,
        bd=1,
        fg="#f2f4f7",
        bg="#465670",
        ).grid(row=self.row-2,column=2,padx=5,pady=5)
        


        Label(self.root,
        font=('sans serif', 20 , 'bold'),
        text="-------------CAR SPEC CATALOG-------------", 
        justify=LEFT,
        bd=1,
        fg="#29293d",
        bg="#a3a5b7"
       ).grid(row=self.row,column=1,pady=10)
        self.row+=1
        before_list=self.row-1
        
        var = StringVar()
        var.set("one") # default value
        
        optionold=OptionMenu(
            self.root,
            var,
            *self.cars,
            command=self.display_specs
        )
        print(str(var))
        optionold.config(width=20,font=('sans serif', 20 , 'bold'),justify=LEFT,bd=1,fg="#29293d",bg="#a3a5b7")
        optionold.grid(row=self.row,column=1)

    def display_specs(self,var):
        self.car_name="Hundai"
        
        txt="Car Name : "+var+"\nModel : "+"2016\n"+"Colors available : "+"Red , Black, White, Grey \
            \n"+"Price : "+"1,00,000\n"+"Number of cars available : "+"200\n"

        Label(self.root,
        font=('sans serif', 12 , 'bold'),
        text="                  ",
        justify=LEFT,
        bd=1,
        fg="#29293d",
        bg="#a3a5b7"
       ).grid(row=self.row+1,column=0,pady=10)


        Label(self.root,
            font=('sans serif', 12 , 'bold'),
            text=txt, 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7"
       ).grid(row=self.row+1,column=0,pady=10)
        
        
        Label(self.root,
            font=('sans serif', 12 , 'bold'),
            text=self.info, 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7"
       ).grid(row=self.row+1,column=1,pady=10)
        
        
        
        self.icon = ImageTk.PhotoImage(Image.open('f.jpg'))
        self.icon_size = Label(self.root)
        self.icon_size.image = self.icon
        self.icon_size.justify=LEFT
        self.icon_size.configure(image=self.icon,width=200,height=200)
        self.icon_size.grid(row=self.row+1,column=2)

        self.root.mainloop()
        
        
         
MainWindow()