from tkinter import *
from PIL import ImageTk, Image

root = Tk()

path = "project/images/nhl_intro.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")

class MainApplication:
    def __init__(self, master):
            root.title("NHL 94")
            root.option_add('*font', ('verdana', 12, 'bold'))
            

class DropDown:
    def __init__(self, master):
            menu = Menu(root)
            root.config(menu=menu)
            subMenu = Menu(menu, tearoff=False) # tearoff removes dashes "-----"
            menu.add_cascade(label="File", menu=subMenu) 
            subMenu.add_command(label="About", command=exit_program) # About section..
            subMenu.add_separator()
            subMenu.add_command(label="Exit", command=exit_program)
            

class Buttons:
    def __init__(self, master):
        fm = Frame(master)
        Button(fm, text='Teams').pack(side=BOTTOM, anchor=W, fill=X, expand=YES)
        Button(fm, text='Random Matchup').pack(side=BOTTOM, anchor=W, fill=X, expand=YES)      
        fm.pack(side=BOTTOM, fill=BOTH, expand=YES)
        

def exit_program():
    sys.exit()


if __name__ == "__main__":
    MainApplication(root)
    DropDown(root)
    Buttons(root)
    root.mainloop()