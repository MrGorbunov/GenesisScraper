import sched
import time
import getpass

from genesis_scraper import *
from file_helper import *
from texting_wrapper import *
from config_handler import *


class Driver:

    def __init__(self):
        self.scrapper = GenesisScraper()
        self.fileHelp = FileHelper()
        #self.texter = TextingWrapper()
        self.file_path = "./data.json"
        self.configHelp = ConfigHandler()

    def login(self, usr, pwd):
        self.scrapper.login(usr, pwd)

    def checkForUpdate(self):
        self.fileHelp.parseWebData(self.scrapper.getData())
        self.fileHelp.parseFileData(self.file_path)

        text_msg = "\n"
        if self.configHelp.doingRecap():
            text_msg += self.getRecapString()
        else:
            text_msg += self.getChangeString()

        if text_msg.strip() != "":
            if self.configHelp.doingSentiment():
                text_msg += self.getSentimentMessage()

            print(text_msg)
            self.texter.sendText(text_msg)

        #at end, we override for next test
        self.fileHelp.writeWebToFile(self.file_path)

    def getRecapString(self):
        data = self.fileHelp.getData()
        total_rec = ""

        for ac_class in data:
            total_rec += ac_class[0]['class'] + ": " + ac_class[0]['grade'] + " -> " + ac_class[1]['grade'] + "\n"

        return total_rec

    def getChangeString(self):
        changes = self.fileHelp.findChanges()

        if not changes:
            return ""

        all_changes = ""

        for change in changes:
            one_change = change[0]['class'] + " changed from a " + change[0]['grade'] + " to a " + \
                         change[1]["grade"] + ".\n"
            all_changes += one_change

        return all_changes

    def getSentimentMessage(self):
        #yes it's inefficient to loop through the array after doing so
        #in getChange / getRecap, but the maintabiltiy is more important
        net_change = 0

        for change in self.fileHelp.findChanges():
            try:
                net_change += float(change[1]["grade"][:-1]) - float(change[0]["grade"][:-1])
            finally:
                pass

        if net_change > 0:
            return "Your grade increased by " + str(net_change) + "%. " + \
                   self.configHelp.getSentimentMessage("good")
        elif net_change < 0:
            return "Your grade decreased by " + str(-net_change) + "%. " + \
                   self.configHelp.getSentimentMessage("bad")
        else:
            return "Your grade didn't change! " + \
                   self.configHelp.getSentimentMessage("neutral")






if __name__ == '__main__':
    s = sched.scheduler(time.time, time.sleep)
    d = Driver()

    d.login(getpass.getpass(prompt="User:"), getpass.getpass())

    def periodicCall(sc):
        d.checkForUpdate()
        s.enter(d.configHelp.getDelay(), 1, periodicCall, (sc,))

    s.enter(0, 1, periodicCall, (s,))
    s.run()
