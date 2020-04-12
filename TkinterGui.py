"""
This program will display a Tkinter GUI
"""

import tkinter
import webbrowser
from tkinter import ttk # using tkinter.tkk is to seperate the code implementing a widget's
                        # behavior from the code implementing its appearance

class TkinterGui:

    def __init__(self):
        self.root = tkinter.Tk()
        self.label_ticker = ttk.Label(self.root,) # This is to display text
        self.button_exit = ttk.Button(self.root)
        self.button_exit.configure(text="quit", command=self.root.quit)
        self.build()
        self.start()

    def start(self):
        self.root.mainloop()

    def build(self):
        self.root.title("RSS News Feed")
        self.label_ticker.grid(row=0, column=0)
        self.button_exit.grid(row=0, column=1)

    def update(self, headline, url):
        """ This should update the news headline """
        self.label_ticker.configure(text=headline)
        self.label_ticker.bind("<Button-1>", lambda e: webbrowser.open_new(url))
    



