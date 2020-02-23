import json
from genesis_scraper import *


class FileHelper:

    def __init__(self):
        self.web_json = {}
        self.file_json = {}

    def parseWebData(self, data):
        self.web_json = {}

        for class_ind in range(0, 10):
            self.web_json[str(class_ind)] = {
                'class': data[class_ind][0],
                'teacher': data[class_ind][1],
                'grade': data[class_ind][2]
            }

    def parseFileData(self, file_path):
        with open(file_path) as f:
            self.file_json = json.load(f)

    def writeWebToFile(self, file_path):
        with open(file_path, 'w') as outfile:
            json.dump(self.web_json, outfile)

    def findChanges(self):
        '''
        Looks for differences between the web_json and file_json
        NOTE: Requires that parseFileData() and parseWebData() have been called!!

        :return: An array of dicts, [ [{old state}, {new state}], ...]
        '''
        # assumes that the data is always in same order
        # which it should because this class generates it
        dif = []

        for ind in range(10):
            if self.web_json[str(ind)] != self.file_json[str(ind)]:
                dif.append([
                    self.file_json[str(ind)],
                    self.web_json[str(ind)]
                ])

        return dif

    def getData(self):
        data = []

        for ind in range(10):
            data.append([
                self.file_json[str(ind)],
                self.web_json[str(ind)]
            ])

        return data

    def cliDebug(self, json_obj):
        for class_ind in range(0, 10):
            loc = json_obj[str(class_ind)]
            print(loc['class'] + " | " + loc['teacher'] + " | " + loc['grade'])

