import unittest
import os
from bs4 import BeautifulSoup
import feedparser



class TestFeedParser(unittest.TestCase):

    def test_build_library(self):
        with open("sample-feed.xml") as xml_file:
            soup = BeautifulSoup(xml_file, "xml") # pip install lxml
        result = feedparser.build_library(soup)

        self.assertEqual(result[0][0], "RSS Resources")
        self.assertEqual(result[0][1], "http://www.rss-specifications.com&quot;&gt;RSS")
        self.assertEqual(result[1][0], "Recommended Desktop Feed Reader Software")
        self.assertEqual(result[1][1], "http://store.esellerate.net/a.asp?c=1_SKU5139890208_AFL403073819&quot;&gt;FeedDemon")



if __name__ == '__main__':
    unittest.main()