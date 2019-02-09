#!/usr/bin/python3
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
        self.button_2 = tk.Button(self.frame, text = 'Hall of Fame', width = 70, command = self.team_window)
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
        # Mp3 theme
        # self.winsound.PlaySound('project/sounnd/theme.wav',winsound.SND_FILENAME)


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
        fileMenu.add_command(label="About", command = lambda: self.popupmsg("NHL94 Tkinter project is made by ponkape. \
        All feedback and development ideas are welcome!"))
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.exit_program)

    def exit_program(self):
            sys.exit(0)

    def popupmsg(self, msg):
        popup = tk.Tk()
        popup.wm_title("About")
        label = tk.Label(popup, text=msg)
        label.pack(fill="x", pady=10)



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

        text_team = tk.Label(parent, text="HALL OF FAME", fg="orange", anchor="n")
        text_team.pack()

        load = Image.open("project/images/east.jpg")
        render = ImageTk.PhotoImage(load)
        home_img = tk.Label(parent, image=render, text="Allstar East", compound=tk.TOP)
        home_img.image = render
        home_img.pack(pady=10)



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
        _map = {'New York Islanders': 'ny_islanders.gif','Montreal Canadiens': 'montreal.gif','Los Angeles Kings': 'los_angeles.gif','Hartford Whalers': 'hartford.gif','Calgary Flames': 'calgary.gif','Buffalo Sabres': 'buffalo.gif','Anaheim Mighty Ducks': 'anaheim.gif','Boston Bruins': 'Boston.gif','Chicago Blackhawks': 'chicago.gif', 'New York Rangers': 'ny_rangers.gif',
                'All-Stars West': 'west.gif','Pittsburgh Penguins': 'pittsburgh.gif','Ottawa Senators': 'ottawa.gif','Florida Panthers': 'florida.gif','Edmonton Oilers': 'edmonton.gif','All-Stars East': 'east.gif','New Jersey Devils': 'devils.gif','Detroit Red Wings': 'detroit.gif','Dallas Stars': 'dallas.gif','Philadelphia Flyers': 'philadelphia.gif', 'Toronto Maple Leafs': 'toronto.gif',
                'Vancouver Canucks': 'vancouver.gif','Winnipeg Jets': 'winnipeg.gif','Washington Capitals': 'washington.gif','Tampa Bay Lightning': 'tampa_bay.gif','St. Louis Blues': 'st_louis.gif','San Jose Sharks': 'sharks.gif','Quebec Nordiques': 'quebec.gif'}
        return os.path.join('project\images', _map[self.name])

class TeamWidget(tk.Label):
    def __init__(self, parent, team, side):
        """
        :param parent: The Parent where this Widget depends on
        :param team: A class Team object
        :p aram side: How to pack this Label to (left|right)
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

        # Setting a class Team object, read its Logo Image and
        # Configure the Lable Widget with text and image

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

        # INIT
        self.__init__Teams()

        # Home team
        self.home_label = TeamWidget(parent, Team('Team Home', None), 'left', )
        # Visitor team
        self.visitor_label = TeamWidget(parent, Team('Team Visitor', None), 'right')


        # Init teams
    def __init__Teams(self):
        self.teams = [Team('Anaheim Mighty Ducks', 'anaheim.jpg'),
                      Team('Chicago Blackhawks', 'chicago.gif'),
                      Team('Philadelphia Flyers', 'philadelphia.gif'),
                      Team('Boston Bruins', 'boston.gif'),
                      Team('Calgary Flames', 'calgary.gif'),
                      Team('Dallas Stars', 'dallas.gif'),
                      Team('Detroit Red Wings', 'detroit.gif'),
                      Team('New Jersey Devils', 'Devils.gif'),
                      Team('All-Stars East', 'east.gif'),
                      Team('All-Stars West', 'west.gif'),
                      Team('Edmonton Oilers', 'edmonton.gif'),
                      Team('Florida Panthers', 'florida.gif'),
                      Team('Hartford Whalers', 'hartford.gif'),
                      Team('Los Angeles Kings', 'los_angeles.gif'),
                      Team('Montreal Canadiens', 'montreal.gif'),
                      Team('New York Islanders', 'ny_islanders.gif'),
                      Team('New York Rangers', 'ny_rangers.gif'),
                      Team('Ottawa Senators', 'ottawa.gif'),
                      Team('Pittsburgh Penguins', 'pittsburgh.gif'),
                      Team('Quebec Nordiques', 'quebec.gif'),
                      Team('San Jose Sharks', 'sharks.gif'),
                      Team('St. Louis Blues', 'st_louis.gif'),
                      Team('Tampa Bay Lightning', 'tampa_bay.gif'),
                      Team('Vancouver Canucks', 'vancouver.gif'),
                      Team('Washington Capitals', 'washington.gif'),
                      Team('Buffalo Sabres', 'buffalo.gif'),
                      Team('Winnipeg Jets', 'winnipeg.gif'),
                      Team('Toronto Maple Leafs', 'toronto.jpg')]


    def genRanTeam(self):
        # Use the initalized Teams from __init__
        self.home_label.team = random.choice(self.teams)
        visitor = None
        # Loop while home == visitor
        while visitor is None or self.home_label.team is visitor:
            visitor = random.choice(self.teams)
        self.visitor_label.team = visitor


if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()