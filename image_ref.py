7

#import statements
from tkinter import *
from PIL import Image

app = Tk()
app.title("Welcome")
root.configure(background="red")
image2 =Image.open('elephant.gif')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
app.geometry('%dx%d+0+0' % (w,h))
#app.configure(background='C:\\Usfront.png')
#app.configure(background = image1)

labelText = StringVar()
labelText.set("Welcome !!!!")
#labelText.fontsize('10')

label1 = Label(app, image=image1, textvariable=labelText,
               font=("Times New Roman", 24),
               justify=CENTER, height=4, fg="blue")
label1.pack()

app.mainloop()