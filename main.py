import tkinter as tk
from PIL import ImageTk, Image
import sys, os
import random

class MainWindow(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent,  *args, **kwargs)
        # Buttons
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.button1 = tk.Button(self.frame, text = 'Random Teams', width = 70, command = self.new_window)
        self.button1.pack(side="bottom", fill="both", expand="yes")
        self.button_2 = tk.Button(self.frame, text = 'Teams', width = 70, command = self.team_window)
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

    def team_window(self):
        self.teams = tk.Toplevel(self.parent)
        self.main = team_window(self.teams)


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

class team_window(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # Frame configurations
        parent.minsize(width=999, height=500)
        parent.title("NHL Teams")
     
        ### Teams-section. Explanation for next solution for showing team logos
        ### http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        ### 
        ### "The problem is that the Tkinter/Tk interface doesn’t handle references to Image objects properly; the Tk widget will hold a reference to the internal object, but Tkinter does not. 
        ### When Python’s garbage collector discards the Tkinter object, Tkinter tells Tk to release the image.
        ### But since the image is in use by a widget, Tk doesn’t destroy it. Not completely. 
        ### It just blanks the image, making it completely transparent…"
        ### 
        ###

        load = Image.open("project/images/east.jpg")
        render = ImageTk.PhotoImage(load)
        home_img = tk.Label(parent, image=render, text="Allstar East", compound=tk.TOP)
        home_img.image = render
        home_img.pack(side="left")

        load = Image.open("project/images/west.jpg")
        render = ImageTk.PhotoImage(load)
        west_img = tk.Label(parent, image=render, text="Allstar West", compound=tk.TOP)
        west_img.image = render
        west_img.pack(side="left")

        load = Image.open("project/images/anaheim.jpg")
        render = ImageTk.PhotoImage(load)
        anaheim_img = tk.Label(parent, image=render, text="Anaheim", compound=tk.TOP)
        anaheim_img.image = render
        anaheim_img.pack(side="left")

        load = Image.open("project/images/boston.jpg")
        render = ImageTk.PhotoImage(load)
        boston_img = tk.Label(parent, image=render, text="Boston", compound=tk.TOP)
        boston_img.image = render
        boston_img.pack(side="left")

        load = Image.open("project/images/buffalo.jpg")
        render = ImageTk.PhotoImage(load)
        buffalo_img = tk.Label(parent, image=render, text="Buffalo", compound=tk.TOP)
        buffalo_img.image = render
        buffalo_img.pack(side="left")



class Team():
    """
    All Team data
    """
    def __init__(self, name, img_filename):
        self.name = name
        self.img_filename = img_filename
        
    @property
    def filepath(self):
        """
        :return: The filepath of this Team Logo image file.
        """
        return self.img_filename

    def __str__(self):
        """
        This is not used in this example, use it for debuging Name - Logo image filename missmatch
        :return: A string describe this Team data
        """
        return "Name: {} Image:{}".format(self.name, self.img_filename)
    
    
class TeamWidget(tk.Label):
    """
    Inherit from tk.Label to build a Team specific Label showing Image and Text
    """
    def __init__(self, parent, team, side):
        """
        :param parent: The Parent where this Widget depends on 
        :param team: A class Team object
        :param side: How to pack this Label to (left|right)
        """
        self._team = None
        super().__init__(parent, Image=None, text=team.name,
                         compound="bottom",
                         fg="yellow",
                         font=("Helvetica", 18)
                         )
        self.pack(side=side)

    @property
    def team(self):
        """
        :return: The class Team object of this TeamWidget 
        """
        return self._team

    @team.setter
    def team(self, team):
        """
        NOTE: This works ONLY for PNG Images!
        
        Setting a class Team object, read its Logo Image and 
        configure the Lable Widget with text and image
        
        :param team: The class Team object related to this TeamWidget 
        :return: None
        """
        self._team = team
        # IMPORTANT: Keep Image reference to not get garbage collected
        self.image = tk.PhotoImage(file=team.filepath)
        super().configure(text=team.name, image=self.image)

class random_team(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.minsize(width=888, height=500)
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
        # Home team
        load = Image.open("project/images/question.jpg") # https://www.charbase.com/fe56-unicode-small-question-mark
        render = ImageTk.PhotoImage(load)
        home_img = tk.Label(parent, image=render)
        home_img.image = render
        home_img.pack(side="left")
        home_label = tk.Label(parent, textvariable = self.home)
        home_label.pack(side="left")
        # Visitor team
        load = Image.open("project/images/question.jpg") # https://www.charbase.com/fe56-unicode-small-question-mark 
        render = ImageTk.PhotoImage(load)
        visitor_img = tk.Label(parent, image=render)
        visitor_img.image = render
        visitor_img.pack(side="right")
        visitor_label = tk.Label(parent, textvariable = self.visitor)
        visitor_label.pack(side="right")


    def __init__Teams(self):
        self.teams = [Team('Allstars East', east.jpg), Team('Allstars West', west.jpg), Team('Anaheim', anaheim.jpg), Team('Boston', boston.jpg), Team('Buffalo', buffalo.jpg), Team('Calgary', calgary.jpg), Team('Chicago', chicago.jpg), Team('Dallas', dallas.jpg), Team('Detroit', detroit.jpg), Team('Edmonton', edmonton.jpg), Team('Florida', florida.jpg),  Team('Hartford', hartford.jpg), Team('Los Angeles', los_angeles.jpg), Team('Montreal', montreal.jpg), Team('NY Islanders', ny_islanders.jpg), Team('NY Rangers', ny_rangers.jpg), Team('Ottawa', ottawa.jpg), Team('Philadelphia', philadelphia.jpg), Team('Pittsburgh', pittsburgh.jpg), Team('Quebec', quebec.jpg), Team('San Jose', sharks.jpg), Team('St. Louis', st_louis.jpg), Team('Tampa Bay', tampa_bay.jpg), Team('Toronto', toronto.jpg), Team('Vancouver', vancouver.jpg), Team('Washington', washington.jpg), Team('Winnipeg', winnipeg.jpg)]
        # Init defaults
        self.home = self.teams[0]
        self.visitor = self.teams[0]
        
        
    def genRanTeam(self): 
        self.__init__Teams()  # Use the initalized Teams from MainWindow..__init__
        self.home = random.choice(self.teams)
        self. visitor = None
        # Loop while home == visitor
        while self.visitor is None or self.home.name is self.visitor.name:
         self.visitor = random.choice(self.teams)
        return
        

if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()