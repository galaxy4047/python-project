from tkinter import *
import tkinter as tk 
import math
from PIL import Image, ImageTk
import sqlite3

class MainWindow:
    def __init__(self): 
        self.t=None
        self.name="Not Specified"
        self.carint="Not Specified"
        self.contact="Not Specified"
        self.address="Not Specified"
        self.cars=[]
        self.conn=sqlite3.connect('visitor.db')
        self.ctrl=self.conn.cursor()
        self.UpdatableStringval=" "
        self.table="Car"
        self.car="car"
        self.model="model"
        self.engine="engine"
        self.color="color"
        self.drive="drive"
        self.seats="seats"
        self.power="power"
        self.fuel="fuel"
        self.price="price"
        self.desc="desc"
        self.img="img"
        #self.ctrl.execute("drop table if exists Car")
        self.ctrl.execute("create table if not exists {tn}({val1} VARCHAR(20) not null,{val2} VARCHAR(20) not null ,{val3} VARCHAR(20) not null,{val4} VARCHAR(20) not null,{val5} VARCHAR(20) not null,{val6} VARCHAR(20) not null,{val7} VARCHAR(20) not null,{val8} VARCHAR(20) not null ,{val9} VARCHAR(20) not null,{val10} VARCHAR(20) not null,{val11} VARCHAR(20) not null )"\
        .format(tn=self.table,val1=self.car,val2=self.model,val3=self.engine,val4=self.color,val5=self.drive,val6=self.seats,val7=self.power,val8=self.fuel,val9=self.price,val10=self.desc,val11=self.img))
        
        ans=self.ctrl.execute("select car from Car")
        self.cars=[]
        for row in ans: 
            self.cars.append(str(row[0]))
        print(type(self.cars))
        

        self.registe_page()
    def delete_db(self):
        self.ctrl.execute("drop table if exists Car")        
    def createdb(self):
        pass
    def insert_tb(self,sense1,sense2,sense3,sense4,sense5,sense6,sense7,sense8,sense9,sense10,sense11):
        self.table="Car"
        self.car=sense1
        self.model=sense2
        self.engine=sense3
        self.color=sense4
        self.drive=sense5
        self.seats=sense6
        self.power=sense7
        self.fuel=sense8
        self.price=sense9
        self.desc=sense10
        self.img=sense11
        try:
            query='insert into Car  values ("'+sense1+'","'+sense2+'","'+sense3+'","'+sense4+'","'+sense5+'","'+sense6+'","'+sense7+'","'+sense8+'","'+sense9+'","'+sense10+'","'+sense11+'")'
            self.ctrl.execute(query)
            self.conn.commit()
        except:
            print("Rolled back")
            self.conn.rollback()
            #self.ctrl.execute("insert into Car values ('car','model','engine','color','drive','seats','power','fuel','price')")
        
            

    def redirecT(self,old_win):
        old_win.destroy()
        self.dispHeaader()
    def registe_page(self):
        r=0
        t=Tk()
        
        t.configure(background="#a3a5b7")
        t.geometry("1400x800")
        global s1,s2,s3,s4
        s1=StringVar()
        s2=StringVar()
        s3=StringVar()
        s4=StringVar()

        Label(t,
            font=('sans serif', 20 , 'bold'), 
            text="                 Wheels To Go\nNear NMAM Institute of Technology\n   Nitte - 574110, Karkala, Udupi", 
            justify=LEFT,
            bd=1,
            fg="#961244",
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
            text=s1, 
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
            text=s2, 
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
            text=s3, 
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
            text=s4, 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7"
        ).grid(row=r,column=1)
        r+=1
        
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
             font=('sans serif', 20, 'bold'), 
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
        self.name=s1.get()
        self.carint=s2.get()
        self.address=s3.get()
        self.contact=s4.get()
        self.t.destroy()
        self.dispHeaader()
    def disp2(self):

        self.t.destroy()
        self.dispinfo()
    def dispinfo(self):
        i=Tk()
        i.configure(background="#a3a5b7")
        
        i.geometry("1400x800")
        txt="                 Wheels To Go\nNear NMAM Institute of Technology\n   Nitte - 574110, Karkala, Udupi"
        
        Label(
            i,
            font=('sans serif', 20 , 'bold'), 
            text=txt, 
            justify=LEFT,
            bd=1,
            fg="#961244",
            bg="#a3a5b7",
       ).grid(row=0,column=1)
        
        
        icon1 = ImageTk.PhotoImage(Image.open('prasanna.jpg'))
        icon_size1 = Label(i)
        icon_size1.image = icon1
        icon_size1.justify=LEFT
        icon_size1.configure(image=icon1,width=200,height=200)
        icon_size1.grid(row=1,column=0,padx=100,pady=20)
        
        icon2 = ImageTk.PhotoImage(Image.open('teju.jpg'))
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
    def get_cars(self):
        return cars  
    def dispHeaader(self):
        
        self.root = Tk()
        self.root.configure(background="#a3a5b7")
        self.root.geometry("1400x800")
        self.row=0
        
        #self.cars=temp
        self.title="                 Wheels To Go\nNear NMAM Institute of Technology\n   Nitte - 574110, Karkala, Udupi"
        self.info="\nMaruti Suzuki India Limited, formerly\nknown as Maruti Udyog Limited, is\nan automobile manufacturer in India.\nIt is a 56.21 owned subsidiary\nof the Japanese car and motorcycle manufacturer\nSuzuki  Motor Corporation. As of July\n2018, it had a market share of 53'%'\nof the Indian passenger car market.\n"
        self.bg="#a3a5b7"
        
        
        Label(self.root,
        font=('sans serif', 20 , 'bold'), 
        text=self.title, 
        justify=LEFT,
        bd=1,
        fg="#961244",
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

        txt1="\n\nDiscover Honda specs and choose the\nmodel you are interested to see. You can\nsee all models with specs for the engine,\nperformance or you can view the photo gallery\n\n\n\n"



        Label(self.root,
        width=43,
        font=('sans serif', 12), 
        text=txt1, 
        justify=LEFT,
        bd=1,
        fg="#f2f4f7",
        bg="#465670",
        ).grid(row=self.row-1,column=1)
        self.row+=1

        txt3="\nUser Name : "+self.name+"\nInterested Car : "+self.carint+"\nContact : "+self.contact+"\nAddress : "+self.address+"\n\n\n\n\n" 

        Label(self.root,
        width=43,
        font=('sans serif', 12), 
        text=txt3, 
        justify=LEFT,
        bd=1,
        fg="#f2f4f7",
        bg="#465670",
        ).grid(row=self.row-2,column=2,padx=2,pady=5)
        


        Label(self.root,
        font=('sans serif', 20 , 'bold'),
        text="-------------CAR SPEC CATALOGUE-------------", 
        justify=LEFT,
        bd=1,
        fg="#29293d",
        bg="#a3a5b7"
       ).grid(row=self.row,column=1,pady=10)
        self.row+=1
        before_list=self.row-1
        

        


        
        var=StringVar(self.root) # default value
        var.set("Hell")
        optionold=OptionMenu(
            self.root,
            var,
            *self.cars,
            command=self.display_specs
        )
        print(str(var))
        optionold.config(width=40,font=('sans serif', 12 , 'bold'),justify=LEFT,bd=1,fg="#29293d",bg="#a3a5b7")
        optionold.grid(row=self.row,column=1)

    def display_specs(self,var):
        
        '''
        self.car="car"
        self.model="model"
        self.engine="engine"
        self.color="color"
        self.drive="drive"
        self.seats="seats"
        self.power="power"
        self.fuel="fuel"
        self.price="price"
'''        
        print(var)
        ans=self.ctrl.execute("select *  from Car where car='"+str(var)+"'")
        for row in ans:
            car=row[0]
            model=row[1]
            engine=row[2]
            color=row[3]
            drive=row[4]
            seats=row[5]
            power=row[6]
            fuel=row[7]
            price=row[8]
            desc=row[9]
            img=row[10]



        txt="Car Name : "+car[10:25]+"\nModel : "+model+"\nEngine Type: "+engine+"\nColors available : "+color \
            +"\nDriving mode : "+drive+"\nSeats : "+seats+"\nPower "+power+"\nFuel : "+fuel+"\nPrice : "+price

        Label(self.root,
        font=('sans serif', 12 , 'bold'),
        text="\n\n\n\n\n\n\n\n\n\n\n\n",
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
            text=desc, 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7"
       ).grid(row=self.row+1,column=1,pady=10)
        
        
        
        self.icon = ImageTk.PhotoImage(Image.open(img))
        self.icon_size = Label(self.root)
        self.icon_size.image = self.icon
        self.icon_size.justify=LEFT
        self.icon_size.configure(image=self.icon,width=200,height=200)
        self.icon_size.grid(row=self.row+1,column=2)
        
        Button(
            self.root,
             font=('sans serif', 10 ), 
            text="Exit...", 
            justify=LEFT,
            bd=1,
            fg="#29293d",
            bg="#a3a5b7",
            command=self.ex
       ).grid(row=8,column=2)
        
        self.root.mainloop()
        
    def ex(self):
        self.root.destroy()
        
         
a=MainWindow()
a.createdb()

desc1="Maruti Suzuki has three \nmanufacturing facilities in India.[22] All \nmanufacturing facilities have a combined\nproduction capacity of 1,700,000 \nvehicles annually. The Gurgaon \nmanufacturing facility has three fully \nintegrated manufacturing plants and is\n spread over 300 acres (1.2 km2).[23] "
'''
        self.car="car"
        self.model="model"
        self.engine="engine"
        self.color="color"
        self.drive="drive"
        self.seats="seats"
        self.power="power"
        self.fuel="fuel"
        self.price="price"
'''
#a.insert_tb("Honda Civic Tourer","2015","Petrol, Diesel","Black , White","Manual","6","142","Hybrid","10,00,000",desc1,"f.jpg")
# a.insert_tb("2015 Honda Civic Tourer 1.6 i-DTEC S","2015","Petrol, Diesel","Black , White","Manual","6","120","Deisel","8,00,000",desc1,"1.jpg")
# a.insert_tb("2015 Honda Civic Tourer 1.6 i-DTEC Comfort","2015","Petrol, Diesel","Black , White","Manual","6","120","Hybrid","11,00,000",desc1,"2.jpg")
# a.insert_tb("2015 Honda Civic Tourer 1.6 i-DTEC Elegance","2015","Petrol, Diesel","Black , White","Manual","6","142","Hybrid","10,00,000",desc1,"3.jpg")
# a.insert_tb("2015 Honda Civic Tourer 1.6 i-DTEC Elegance Business Edition","2015","Petrol, Diesel","Black , White","Manual","6","142","Hybrid","10,00,000",desc1,"4.jpg")
# a.insert_tb("2015 Honda Civic Tourer 1.6 i-DTEC Elegance Black Edition","2015","Petrol, Diesel","Black , White","Manual","6","142","Hybrid","15,00,000",desc1,"5.jpg")
# a.insert_tb("2015 Honda Civic Tourer 1.6 i-DTEC Lifestyle","2015","Petrol, Diesel","Black , White","Automatic","6","120","Hybrid","10,00,000",desc1,"6.jpg")
# a.insert_tb("2015 Honda Civic Tourer 1.8 Executive","2015","Petrol, Diesel","Black , White","Manual","5","142","Petrol","8,00,000",desc1,"7.jpg")
# a.insert_tb("2015 Honda Civic Tourer 1.8 Lifestyle","2015","Petrol, Diesel","Black , White","Manual","6","142","Petrol","9,00,000",desc1,"8.jpg")

#a.delete_db()

#a.insert_tb(1,2,3,4,5,6,7,8,9)