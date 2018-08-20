from tkinter import * # does not work id the file name is tkinter.py
root=Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Press here! 1", fg="red")
button2 = Button(topFrame, text="Press here! 2", fg="yellow")
button3 = Button(topFrame, text="Press here! 3", fg="green")
button4 = Button(bottomFrame, text="Press here! 4", fg="grey")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()