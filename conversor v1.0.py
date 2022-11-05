from tkinter import *
import tkinter as ttk
import PIL
from PIL import Image
from tkinter import filedialog

master = Tk()
master.geometry('500x150')
def file_select():
    global image   
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
def convert_png(img):
    final_path = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*")))
    img.save(final_path.name)
def convert():
    if value_inside.get() == 'png':
        convert_png(image)
    else:
        print('jpg')    
    return None


options_list =['png', 'jpg']

value_inside = ttk.StringVar(master)
value_inside.set("Select an Option")

question_menu = ttk.OptionMenu(master, value_inside, *options_list)
question_menu.place(x = 175, y = 50)

select_button = ttk.Button(master, text='Select File', command=file_select)
submit_button = ttk.Button(master, text='Convert', command=convert)
submit_button.place(x = 350, y = 50)
select_button.place(x = 50, y = 50 )
  
master.mainloop()
