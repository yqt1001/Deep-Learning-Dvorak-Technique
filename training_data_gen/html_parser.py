from html.parser import HTMLParser
from image import Image

# parses in the directories


class StormPage(HTMLParser):
    url = None
    desc = None
    images = []

    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "a" and len(attrs) > 0 and len(attrs[0]) > 1 and attrs[0][1][0].isdigit():
            self.url = attrs[0][1]

    def handle_endtag(self, tag):
        if tag == "a" and self.url is not None and self.desc is not None:
            self.images.append(Image(self.url, self.desc))
            self.url = None
            self.desc = None

    def handle_data(self, data):
        self.desc = data