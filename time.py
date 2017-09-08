import os
from twython import Twython
from datetime import datetime

# set twitter account
CONSUMER_KEY = 'sDfbKAwU5wkokdLwVYNr3ZjaX'
CONSUMER_SECRET = 'ZYub8Jk6jqpKmz5T4Ljn7gicNNtHaTcy8RjCKOYiPCvmP19GKJ'
ACCESS_KEY = '351582959-EO5JC4JZzIzWbTCCQDmRkHoTppbXZPf7piheMqiI'
ACCESS_SECRET = '6SqQfl91NZx8sbBObCdofhwAMBUrDHhwzCauAmFeV5bQW'
api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# get time string
nowStr = datetime.now().strftime("------------%H:%M------------")

# tweet time
api.update_status(status=nowStr)
