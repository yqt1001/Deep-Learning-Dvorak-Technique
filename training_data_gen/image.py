from datetime import datetime


class Image():
    def __init__(self, url, desc):
        self.url = url

        try:
            # parse description
            if "mtsat-2" in desc:
                desc = desc.replace("mtsat-2", "mtsat2")

            desc = desc.replace(".", "-").split("-")

            self.date = desc[0]
            self.ztime = desc[1]
            self.time = datetime.strptime(desc[0] + " " + desc[1] + " +0000", "%Y%m%d %H%M %z")
            self.satellite = desc[2]
            self.name = desc[5]
            self.wind = int(desc[6][:len(desc[6])-3])  # convert from '100kts' to '100'

            # in the case of 2005 and 2004 without pc values just assume all images are perfect unfortunately
            if "pc" in desc[10]:
                self.pc = int(desc[10][:len(desc[10]) - 2])  # convert from '100pc' to '100'
            else:
                self.pc = 100

            self.valid = True
        except Exception:
            self.valid = False

    def to_string(self):
        return self.date + self.ztime + " " + self.name + " " + str(self.wind) + "kts " \
               + self.satellite + " " + str(self.pc) + "pc"
