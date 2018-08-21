from tkinter import * 

# Create main window by creating an instance of Tk
# Global import must be fixed. Use tkinter by name and prefix tkinter commands with module names
# import tkinter as tk

root=Tk()

topFrame = Frame(root)
# Put widget inside a frame with .pack()
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Press here! 1")
button2 = Button(topFrame, text="Press here! 2")
button3 = Button(topFrame, text="Press here! 3", fg="green")
button4 = Button(bottomFrame, text="Press here! 4", fg="grey")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


# Actions needed..

def doNothing():
    print("Okay okay, not yet")

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu) # Dropdown
subMenu.add_command(label="New Project..", command=doNothing)
subMenu.add_command(label="New..", command=doNothing)
subMenu.add_separator() 
subMenu.add_command(label="Exit", command=doNothing)

root.mainloop()