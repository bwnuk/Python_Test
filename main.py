from tkinter import *

def doNothing():
    print("OK")

root = Tk()

# *** MENU ***

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

# *** TOOLBAR ***

toolbar = Frame(root, bg="blue")

insertButton = Button(toolbar, text="Insert image", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)

printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# *** Status Bar ***

status = Label(root, text="Doing nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()