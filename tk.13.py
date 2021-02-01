import tkinter as tk

root = tk.Tk()
root.geometry('300x200')
lb = tk.Label (text='this is a label,this is a label,this is a label')
ms = tk. Message(text='this is a message .this is a message.this is a message')
[widget.pack() for widget in (lb,ms)]

root.mainloop()