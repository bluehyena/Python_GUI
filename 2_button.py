from tkinter import *

def btncmd():
    print("Button clicked")

root = Tk()
root.title("GUI")

btn1 = Button(root, text=("버튼1"))
btn1.pack()

# 버튼의 여백정하기, padx = 가로 pady = 높이
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# width, height 고정크기, 버튼 크기를 정함
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

# fg = 글씨색, bg = 배경색
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="img.png")

btn6 = Button(root, image=photo)
btn6.pack()

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()