import os
from twython import Twython
from datetime import datetime

# set twitter account
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# get time string
nowStr = datetime.now().strftime("------------%H:%M------------")

# tweet time
api.update_status(status=nowStr)
