from tkinter import *
from PIL import ImageTk, Image

# Buttons

class App:
    def __init__(self, master):
        fm = Frame(master)
        Button(fm, text='Teams').pack(side=BOTTOM, anchor=W, fill=X, expand=YES)
        Button(fm, text='Random Matchup').pack(side=BOTTOM, anchor=W, fill=X, expand=YES)      
        fm.pack(side=BOTTOM, fill=BOTH, expand=YES)

# Main window
root = Tk()
root.title("NHL 94")
root.configure(background='grey')

root.option_add('*font', ('verdana', 12, 'bold'))
display = App(root)

path = "nhl.jpg"

# Tkinter-compatible photo image
img = ImageTk.PhotoImage(Image.open(path))

# Widget 
panel = Label(root, image = img)

# Put widget inside a frame with .pack()
panel.pack(side = "bottom", fill = "both", expand = "yes")


# Dropdown Menu

def exit_program():
    sys.exit()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu, tearoff=False) # tearoff removes dashes "-----"
menu.add_cascade(label="File", menu=subMenu) 
subMenu.add_command(label="About", command=exit_program) # About section..
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit_program)


root.mainloop()