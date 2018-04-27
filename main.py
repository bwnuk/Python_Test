from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Click 0", fg="red")
button2 = Button(topFrame, text="Click 1", fg="blue")

button3 = Button(bottomFrame, text="Click 0", fg="green")
button4 = Button(bottomFrame, text="Click 1", fg="black")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()