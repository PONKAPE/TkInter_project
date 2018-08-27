from tkinter import *
from PIL import ImageTk, Image

# Main window
root = Tk()
root.title("NHL 94")
root.geometry("700x400")
root.configure(background='grey')

path = "nhl.jpg"

# Tkinter-compatible photo image
img = ImageTk.PhotoImage(Image.open(path))

# Widget 
panel = Label(root, image = img)

# Put widget inside a frame with .pack()
panel.pack(side = "bottom", fill = "both", expand = "yes")


# Drop down Menu

def exit_program():
    sys.exit()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu) 
subMenu.add_command(label="About", command=exit_program) # About section..
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit_program)


root.mainloop()