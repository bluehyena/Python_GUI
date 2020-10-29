from tkinter import *

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

root = Tk()
root.title("GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력하세요")

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()