from tkinter import *

def doNothing():
    print("OK")

root = Tk()

menu_m = Menu(root)
root.config(menu=menu_m)

subMenu = Menu(menu_m)
menu_m.add_cascade(label="File", menu = subMenu)
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="New..", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu_m)
menu_m.add_cascade(label="Edit", menu = editMenu)
editMenu.add_command(label="New..", command=doNothing)

root.mainloop()