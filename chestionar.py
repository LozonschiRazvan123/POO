from tkinter import *
from tkinter.ttk import *
root=Tk()
root.geometry('300x400')
root.title('Chestionar')
def functie():
    if entry_nume.get==None and entry_parola.get==None:
        afis=Label(root,text="Ati salvat datele")
        afis.grid()
    else:
        afis1=Label(root,text="Eroare")
        afis1.grid()
nume=Label(root,text='Nume Prenume  ')
nume.grid(sticky=W)
parola=Label(root,text="Parola")
parola.grid(sticky=W,pady=5)
submit=Button(root,text='Submit',command=functie)
submit.grid()
entry_nume=Entry(root,width=50)
entry_nume.grid(row=0,column=1)
entry_parola=Entry(root,show='*',width=50)
entry_parola.grid(row=1,column=1)
root.mainloop()