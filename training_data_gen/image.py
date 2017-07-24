from datetime import datetime


class Image():
    def __init__(self, url, desc):
        self.url = url

        # parse description
        desc = desc.replace(".", "-").split("-")

        self.date = desc[0]
        self.ztime = desc[1]
        self.time = datetime.strptime(desc[0] + " " + desc[1] + " +0000", "%Y%m%d %H%M %z")
        self.satellite = desc[2]
        self.name = desc[5]
        self.wind = int(desc[6][:len(desc[6])-3])  # convert from '100kts' to '100'
        self.pc = int(desc[10][:len(desc[10])-2])  # convert from '100pc' to '100'
