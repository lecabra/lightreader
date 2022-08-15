import tkinter as tk
from tkinter import messagebox
from PIL import Image
import glob
import sys
from time import sleep
import back_handler as bh

# create a tkinter class
class LightReader(tk.Tk):
    # constructor
    def __init__(self, path):
        # call the constructor of the parent class
        tk.Tk.__init__(self)
        # set the title of the window
        self.title(f"LightReader v0.1 - {path[:-1]}")
        # set the size of the window
        self.geometry("500x650")
        self.resizable(False, False)
        
        self.page = 0
        self.files = glob.glob(f"{path}*.png")

        self.resize_images()
        try:
            self.create_canvas()
            self.create_buttons()
        except:
            messagebox.showerror("Error", "No images found in this folder!")
            self.back()
        
    # create canvas
    def create_canvas(self):
        self.cv = tk.Canvas(self, width=500, height=500)
        self.cv.pack()
        # add image to cv
        self.img = tk.PhotoImage(file=self.files[self.page])
        self.display = self.cv.create_image(250, 250, image=self.img)

    # next button
    def next(self):
        if self.page < len(self.files)-1:
            self.page += 1

            self.img = tk.PhotoImage(file=self.files[self.page])
            self.cv.itemconfig(self.display, image=self.img)
            self.update()

    # previous button
    def prev(self):
        if self.page > 0:
            self.page -= 1
            self.img = tk.PhotoImage(file=self.files[self.page])
            self.cv.itemconfig(self.display, image=self.img)
            self.update()

    # auto button
    def auto(self):

        for i in range(len(self.files)):
            self.img = tk.PhotoImage(file=self.files[i])
            self.cv.itemconfig(self.display, image=self.img)
            self.update()
            sleep(int(self.entry.get())/1000)

    def back(self):
        self.destroy()
        bh.back()

    def resize_images(self):
        for i in range(len(self.files)):
            img = Image.open(self.files[i])
            img = img.resize((500, 500))
            img.save(self.files[i])
            
    # create buttons
    def create_buttons(self):
        self.next_button = tk.Button(self, text=">>>", command=self.next)
        self.next_button.place(x=400, y=500)

        self.prev_button = tk.Button(self, text="<<<", command=self.prev)
        self.prev_button.place(x=100, y=500)

        self.auto_button = tk.Button(self, text="Auto", command=self.auto)
        self.auto_button.place(x=250, y=500)
        
        self.entry = tk.Entry(self)
        self.entry.place(x=250, y=550)
        self.entry.insert(tk.END, "1000")
        
        self.label = tk.Label(self, text="Delay (ms)")
        self.label.place(x=270, y=570)

        self.exit = tk.Button(self, text="Exit", command=self.back)
        self.exit.place(x=0, y=600)

if __name__ == '__main__':
    print('This is a module. Please run main.py')