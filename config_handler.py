import json
import random


#seconds per unit (sec, min, hour, day, week)
TIME_MULTIPLIER = {
    "S": 1,
    "M": 60,
    "H": 60 * 60,
    "D": 60 * 60 * 24,
    "W": 60 * 60 * 24 * 7
}


class ConfigHandler:

    def __init__(self):
        settings = {}
        with open("config.json") as f:
            settings = json.load(f)

        self.delay = int(settings['delay'][:-1])
        self.delay *= TIME_MULTIPLIER[settings['delay'][-1].upper()]

        self.sentiment = settings['sentimental messages'].upper() == "TRUE"
        self.messages = {}
        with open("config_sentiments.json") as f:
            self.messages = json.load(f)

        self.recap = settings['recap mode'].upper() == "TRUE"

    def getDelay(self):
        return self.delay

    def doingSentiment(self):
        return self.sentiment

    def getSentimentMessage(self, state):
        '''

        :param state: "good", "neutral", or "bad"
        :return:
        '''
        return self.messages[state.lower()][random.randint(0, len(self.messages[state.lower()]) - 1)]

    def doingRecap(self):
        return self.recap

