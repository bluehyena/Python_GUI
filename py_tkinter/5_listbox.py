from tkinter import *

def btncmd():
    listbox.delete(END)

root = Tk()
root.title("GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0) #height = 3 이면 사과,딸기,바나나 출력됨
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()