from tkinter import *

root = Tk()
root.title('Getting Started with widgets')
root.geometry("400x300")
text_box = Text(height=3)
entry = Entry()


def run():
    text_box.delete("1.0", "end")
    input = entry.get()
    text_box.insert(END,float(input)*2.54)

btn = Button(text="Run", command=run, height=1,bg = "#030B76", fg='white')
entry.pack()
btn.pack()
text_box.pack()

root.mainloop()