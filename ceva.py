from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("First program")
root.geometry('350x200')
menu=Menu(root)
item=Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File',menu=item)
root.configure(menu=menu)
Style().configure('TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'red')
Style().map('TButton',foreground=[('active','!disabled','green')],background=[('active','black')])
label=Label(root,text="Am reusit?")
label.grid()
txt=Entry(root,width=10)
txt.grid(column=1,row=0)
def clicked():
    res="You wrote "+txt.get()
    label.configure(text = res)
btn=Button(root, text='Click Me!', style='TButton',command=clicked)
btn.grid(column=2,row=0)
root.mainloop()