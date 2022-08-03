# from tkinter import *
# from tkinter.ttk import *
# root=Tk()
# root.geometry('300x400')
# root.title("simulare")
# x=StringVar()
# check_button=Checkbutton(root,text='Mesaj',variable=x).pack()
# # root.mainloop()
# x = int(input())
#
# dictt = {}
#
# for i in range(x):
#     text = input().split(" ")
#     dictt[text[0]] = text[1]
#
# # while True:
# #     try:
# #         inpt = input()
# #         if inpt in dictt:
# #             print(inpt+"="+dictt[inpt])
# #         else:
# #             print("Not found")
# #     except EOFError:
# #         break
# print('sam 99912222'.split())


strArr=["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
l1 = strArr[0].replace(' ', '').split(",")
l2 = strArr[1].replace(' ', '').split(",")
l=[i for i in l1 if i in l2]
print(l)