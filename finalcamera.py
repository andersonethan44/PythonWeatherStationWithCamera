import picamera
import time 
import tweepy
import sys
import datetime
import os
import subprocess
from Adafruit_CCS811 import Adafruit_CCS811
import pendulum
#PiCamera() class instance
camera = picamera.PiCamera()
imageNumber = 0;

#Function that waits x seconds  
def wait (x):
        time.sleep(x)
#Sets up api and connection to twitter via tweepy
def get_api(cfg):
        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['c$
        auth.set_access_token(cfg['access_token'], cfg['access$
        return tweepy.API(auth)


#function that tweets an image and a message
def tweet_image(image, message):

        cfg  = {
        "consumer_key"        : "WXOkKZt31Fo0coGRctz5Mgh7P",
        "consumer_secret"     : "DN99eVXotuGvckaR8IyDYbNz8ewjW$
        "access_token"        : "929481731429855235-kLgX68NdCS$
        "access_token_secret" : "BHc2n5khARAOzDajBLUiJzEjUlHaN$
        } 
        api = get_api(cfg)
        api.update_with_media(image,message)
        os.remove(image)
ccs = Adafruit_CCS811()
while 1:
        filename = 'images/image'+str(imageNumber)+'.jpg'
        
        dateAndTime = pendulum.now('EST');
        print(str(dateAndTime.to_datetime_string()))
       
        camera.capture(filename)
        co2= ""
        a = subprocess.check_output('sudo temper-poll',shell=T$
        i = 0
        while i<5:
                if ccs.available():
                        temp = ccs.calculateTemperature()
                if not ccs.readData():
                        co2= "CO2: ", ccs.geteCO2(), " ppm"
                        #, TVOC: ", ccs.getTVOC(), " temp: ", $
                wait(2)
                i=i+1
        print(str(dateAndTime.to_datetime_string())+a[25:])
        co2formatted= ""
        co2formatted = co2formatted + str(co2[0])
        co2formatted = co2formatted + str(co2[1])
        co2formatted = co2formatted + str(co2[2])
        print(str(co2formatted))

        tweet_image(filename, str(dateAndTime.to_datetime_stri$
        #code needed here to create period tweeting, use wait($
        break;