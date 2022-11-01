from typing import final
import PIL
from PIL import Image
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

image = Image.open(file_path)

def convert(img):
    final_path = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*")))
    img.save(final_path.name)
    
convert(image)  

