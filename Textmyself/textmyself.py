# textmyself.py - Defines the textmyself() function that texts a message
# passed to it as a string
# This module must be imported as "textmyself" in order to run other scripts

#Preset values: place the values for your account here
accountSID = '############'
authToken = '#############'
twilioNumber = '##########'
myNumber = '###########'

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
