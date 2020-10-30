from tkinter import *

def change():
    label1.config(text="Goodbye World!")
    
    global photo2
    photo2 = PhotoImage(file="img2.png")
    label2.config(image=photo2)

root = Tk()
root.title("GUI")
root.geometry("640x480")

label1 = Label(root, text="Hello World!")
label1.pack()

photo = PhotoImage(file="img.png")
label2 = Label(root, image=photo)
label2.pack()

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()