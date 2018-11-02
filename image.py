from tkinter import *
from PIL import Image, ImageTk
 
class TryImage:
    def __init__(self, parent, image_path=None):
        self.image_path = image_path
        self.parent = parent
 
    def image_to_label(self):
        self.bar = Frame(self.parent, relief=RIDGE, borderwidth=5)
        self.bar.pack(fill=X, side=TOP)
 
        self.bar.columnconfigure(0, weight=1)
        self.bar.rowconfigure(0, weight=1)
 
        self.icon = ImageTk.PhotoImage(Image.open(self.image_path))
        self.icon_size = Label(self.bar)
        self.icon_size.image = self.icon
        self.icon_size.configure(image=self.icon)
        self.icon_size.pack(side=LEFT)
 
if __name__ == '__main__':
    root = Tk()
    ti = TryImage(root, 'sh.png')
    ti.image_to_label()
    root.mainloop()