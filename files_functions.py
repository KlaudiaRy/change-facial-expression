from tkinter import *
from PIL import Image
from tkinter import filedialog
import numpy as np
import tkinter as tk

def pick_photo():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="samples", title="Select picture", filetypes=(("jpg files","*.jpg"),("all files","*.*")))
    image_name= root.filename
    root.destroy()
    img = np.array(Image.open(image_name).convert('L'))
    img2 = Image.fromarray(img)
    img3=img2.resize((48, 48))
    img3.save('tmp/greyscale.jpg', "JPEG")
    return 'tmp/greyscale.jpg'

def display_info():
    root = tk.Tk()
    T = tk.Text(root, height=50, width=150)
    T.pack()
    f = open("information.txt", "r")
    text=f.read()
    T.insert(tk.END, text)
    f.close()
    tk.mainloop()