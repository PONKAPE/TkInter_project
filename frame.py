import tkinter as tk # Python 3
from PIL import ImageTk, Image

# Main window
window = tk.Tk()
window.title("NHL 94")
window.geometry("700x400")
window.configure(background='grey')

# Image path
path = "nhl.jpg"

# Tkinter-compatible photo image
img = ImageTk.PhotoImage(Image.open(path))

# Widget 
panel = tk.Label(window, image = img)

# Put widget inside a frame with .pack()
panel.pack(side = "bottom", fill = "both", expand = "yes")


window.mainloop()