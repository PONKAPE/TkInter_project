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
        # Title, font & window size
        root.title("NHL 94") 
        root.option_add('*font', ('verdana', 16, 'bold'))
        root.geometry("700x450")
        root. resizable(0, 0) # Don't allow resizing
        # NHL-Image
        load = Image.open("project/images/nhl_intro.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def new_window(self): 
        self.newWindow = tk.Toplevel(self.parent)
        self.main = random_team(self.newWindow)


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

class random_team(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.minsize(width=777, height=500)
        parent.title("RANDOMIZE")
        # TEXT
        text_1 = tk.Label(parent, text="VS", fg="red", anchor="center")
        text_1.place(relx=.5, rely=.5, anchor="center") 
        text_2 = tk.Label(parent, text="RANDOM GAME", fg="green", anchor="n")
        text_2.pack(side="top") 
        # Button for randomize
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.randomButton = tk.Button(self.frame, text = 'RANDOM', command=self.genRanTeam)
        self.randomButton.pack(side="bottom")
        self.frame.pack(side="bottom")
        self.home = tk.StringVar()
        self.visitor = tk.StringVar()
        # Team 1 input
        home_label = tk.Label(parent, textvariable = self.home)
        home_label.pack(side="left")
        # Team 2 input-field
        visitor_label = tk.Label(parent, textvariable = self.visitor)
        visitor_label.pack(side="right")
        

    def genRanTeam(self):
        x = random.choice(['Allstars East', 'Allstars West', 'Anaheim', 'Boston', 'Buffalo', 'Calgary', 'Chicago', 'Dallas', 'Detroit', 'Edmonton', 'Florida', 'Hartford', 'Los Angeles', 'Montreal', 'New Jersey', 'NY Islanders', 'NY Rangers', 'Ottawa', 'Philadelphia', 'Pittsburgh', 'Quebec', 'San Jose', 'St. Louis', 'Tampa Bay', 'Toronto', 'Vancouver', 'Washington', 'Winnipeg'])
        y = random.choice(['Allstars East', 'Allstars West', 'Anaheim', 'Boston', 'Buffalo', 'Calgary', 'Chicago', 'Dallas', 'Detroit', 'Edmonton', 'Florida', 'Hartford', 'Los Angeles', 'Montreal', 'New Jersey', 'NY Islanders', 'NY Rangers', 'Ottawa', 'Philadelphia', 'Pittsburgh', 'Quebec', 'San Jose', 'St. Louis', 'Tampa Bay', 'Toronto', 'Vancouver', 'Washington', 'Winnipeg'])
        self.home.set(x)
        self.visitor.set(y)
        return
        


if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()