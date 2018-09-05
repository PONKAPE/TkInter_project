import tkinter as tk
from PIL import ImageTk, Image
import sys


class MainWindow(tk.Frame):
    counter = 0

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent,  *args, **kwargs)
        # Buttons
        self.button1 = tk.Button(self, text="Random Matchup",
                                 command=self.hockey_teams)
        self.button1.pack(side="bottom", fill="both")
        self.button2 = tk.Button(self, text="Teams",
                                 command=self.random_teams)
        self.button2.pack(side="bottom", fill="both")
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


    def hockey_teams(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def random_teams(self): 
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
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


