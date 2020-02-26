import json

#Outside of the repo (to avoid accidental commits), there is a credentials.json file
#It looks like this;
'''
Genesis:
{"user": ..., "pass": ...}
Twilio:
{"account-sid": ..., "auth-token": ...,
 "num-to": ...., "num-from": ....}
'''

class CredentialFetcher:

    def __init__(self, file_path):
        with open(file_path) as f:
            json_data = json.load(f)

        self.genesisUser = str(json_data['Genesis']['user'])
        self.genesisPass = str(json_data['Genesis']['pass'])

        self.twilioSid = str(json_data['Twilio']['account-sid'])
        self.twilioAuth = str(json_data['Twilio']['auth-token'])
        self.numTo = str(json_data['Twilio']['num-to'])
        self.numFrom = str(json_data['Twilio']['num-from'])

