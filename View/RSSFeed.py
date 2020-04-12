import feedparser
from tkinter import *
import webbrowser



feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml?edition=us")

feed_title = feed['feed']['title']
feed_entries = feed.entries


def callback(event, article_link):
    webbrowser.open_new(article_link)


root = Tk()
text = Text(root)
for entry in feed.entries:

    article_title = entry.title
    article_link = entry.link
    article_published_at = entry.published # Unicode string
    article_published_at_parsed = entry.published_parsed # Time object
    #article_author = entry.author
    content = entry.summary
    #article_tags = entry.tags

    print ("{}[{}]".format(article_title, article_link))
    print ("Published at {}".format(article_published_at))
    #print ("Published by {}".format(article_author))
    print("Content {}".format(content))
    #print("catagory{}".format(article_tags))

    link = Label(root, text="{}\n".format(article_title), fg="blue", cursor="hand2")
    link.pack()

    link.bind("<Button-1>" ,lambda event, link=article_link: callback(event, link))

text.tag_config("here")
root.mainloop()