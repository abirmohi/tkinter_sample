import tkinter as tk

def action_btn_press():
    print('Button was pressed')

root = tk.Tk()
root.title('widget creation')
root.geometry('350x150')
lb = tk.Label(text='Label')
bt = tk.Button(text='BUTTON-1',command=action_btn_press)
lb.pack()
bt.pack()
root.mainloop()