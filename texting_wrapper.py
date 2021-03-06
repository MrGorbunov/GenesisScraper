from twilio.rest import Client


class TextingWrapper:

    def __init__(self, creds):
        # Your Account Sid and Auth Token from twilio.com/console
        # DANGER! This is insecure. See http://twil.io/secure
        account_sid = creds.twilioSid
        auth_token = creds.twilioAuth

        self.numTo = creds.numTo
        self.numFrom = creds.numFrom

        if account_sid == '' or auth_token == '':
            print("WARNING: Twilio information is not present!! Texting is not functional")

        self.client = Client(account_sid, auth_token)

    def sendText(self, string):
        message = self.client.messages \
                        .create(
                             body=string,
                             from_=self.numFrom,
                             to=self.numTo
                         )
