import tkinter as tk
from PIL import ImageTk, Image
import sys


class MainWindow(tk.Frame):
  #  counter = 0

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent,  *args, **kwargs)
        # Buttons
        self.parent = parent
        self.navbutton = NavButton(self)
        self.navbutton.pack(side="bottom", fill="both")
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


class NavButton(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.teamsBtn = tk.Button(self, text='Teams', command=self.hockey_teams)
        self.randomBtn = tk.Button(self, text='Random Matchup', command=self.random_teams)
        self.teamsBtn.pack(fill="both")
        self.randomBtn.pack(fill="both")

    def hockey_teams(self):
        t = tk.Toplevel(self)
        t.wm_title("Teams Section")
        l = tk.Label(t, text="Teams")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def random_teams(self): 
        t = tk.Toplevel(self)
        t.wm_title("RANDOM")
        l = tk.Label(t, text="Randomize")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)


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


