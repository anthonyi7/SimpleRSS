import TkinterGui
import tkinter
import feedparser
import threading
import time

from tkinter import ttk

# Variables
TIME_LOOP = 2 # Seconds


def run_gui(urls):
    library = []
    for url in urls:
        library += feedparser.parse(url)
    gui = TkinterGui.TkinterGui()
    cycle_thread = threading.Thread(target=cycle_news, args=[gui, library])
    cycle_thread.start()
    gui.start()

def cycle_news(gui, library):
    while True:
        for item in library:
            gui.update(item[0], item[1])
            time.sleep(TIME_LOOP)


if __name__ == '__main__':
    urls = ['http://feeds.bbci.co.uk/news/rss.xml']
    
    run_gui(urls)
    