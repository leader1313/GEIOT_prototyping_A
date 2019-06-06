from w1thermsensor import W1ThermSensor
import tweepy
import datetime
import time

sensor = W1ThermSensor() #module name(raspberry pi)
consumer_key="g4xlCJdZajLQoEimXa7iSA6kR"
consumer_secret="l6MpFBnXvs9vNGXkp0lSqXSPNWumGNbbOKd4FDgieOGCYP0njq"
access_token="1136576006163013632-eFDl22eFjNA5Dg77n71jNn3syTeL89 "
access_token_secret="qcmNx1mzFnxtNT0cITdHK2JaLWNHoFdtzxB9wkTgbO33a"
auth = tweepy.OAthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

while(True):
    celsius = sensor.get_temperature()
    now = datetime.datetime.now()
    api.update_status(status="Time: {0}:{1}:{2}, Temperature: {3} degrees celsius".format(now.hour, now.minute, now.second, celsius))
    time.sleep(15) #update for 15sec
