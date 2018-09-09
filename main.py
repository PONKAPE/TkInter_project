import tkinter as tk
from PIL import ImageTk, Image
import sys
import random

class MainWindow(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent,  *args, **kwargs)
        # Buttons
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.button1 = tk.Button(self.frame, text = 'Random Teams', width = 70, command = self.new_window)
        self.button1.pack(side="bottom", fill="both", expand="yes")
        self.button_2 = tk.Button(self.frame, text = 'Teams', width = 70, state = tk.DISABLED)
        self.button_2.pack(side="bottom", fill="both", expand="yes")
        self.frame.pack(side="bottom", fill="both")
        # Menu Bar
        menubar = MenuBar(self)
        root.configure(menu=menubar)
        root.title("NHL 94") 
        root.option_add('*font', ('verdana', 12, 'bold'))
        root.geometry("700x450")
        # NHL-Image
        load = Image.open("project/images/nhl_intro.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def new_window(self): 
        self.newWindow = tk.Toplevel(self.parent)
        self.main = random_team(self.newWindow)

class random_team(tk.Frame):
    def __init__(self, parent):
        parent.minsize(width=666, height=500)
        parent.title("RANDOMIZE")
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.quitButton = tk.Button(self.frame, text = 'Quit')
        self.quitButton.pack()
        self.frame.pack()


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="About", command=self.exit_program)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.exit_program)

    def exit_program(self):
        sys.exit(0)


if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()