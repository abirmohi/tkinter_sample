import tkinter as tk

def action_btn_press():
    print('ボタンが押されました')
def action_btn_press():
    print('モヒ')

root = tk.Tk()
root.title('アクション組み込み')
root.geometry('350x150')
lb = tk.Label(text='ラベル')
bt1 = tk.Button(text='Button')
bt2 = tk.Button (text='Button')
bt = tk.Button(text='ボタン',command=action_btn_press)
bt = tk.Button(text='ボタン',command=action_btn_press)


lb.pack()
bt1.pack()
bt2.pack()
bt.pack()
root.mainloop()