import tkinter as tk
from PIL import ImageTk, Image
import sys


class MainWindow(tk.Frame):
    counter = 0

    def __init__(self, showImg, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button1 = tk.Button(self, text="Create new window",
                                 command=self.create_window)
        self.button1.pack(side="top")
        root.title("NHL 94")
        root.option_add('*font', ('verdana', 12, 'bold'))
        root.geometry("500x500")
        load = Image.open("project/images/nhl_intro.jpg")
        render = ImageTk.PhotoImage(load)
        # labels can be text or images
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=100, y=100)

    

    def create_window(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)


if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
