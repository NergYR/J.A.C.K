import datetime as dt
import json
import os as os
import sys as sys
import pytz
import pyttsx3 as tts 
config_file = "C:/Users/energ/Desktop/Code/Python/J.A.C.K/config.json"

timezone = pytz.timezone(json.load(open(config_file))['timezone'])


class Time :
    d = dt.datetime.now(timezone)





    def sayHourOfDay():
        '''
        ## SayHourOfDay() 
        This function is a tts function, say the hour of the day \n
        return string : the hour of the day
        
        '''
        engine = tts.init()
        engine.say("il est actuellement " + Time.d.strftime("%H") + "heure")
        engine.runAndWait()
        print(Time.d.strftime("%H"))
        return Time.d.strftime("%H")


    def sayDateTime():
        '''
        ## SayDateTime()
        This function is a tts function, say the date and time of the day \n
        return string : the date and time of the day format 'Hour:Minute'
        '''
        engine = tts.init()
        engine.say("il est actuellement " + Time.d.strftime("%H") + "heure" + Time.d.strftime("%M"))
        engine.runAndWait()
        print(Time.d.strftime("%H") + ":" + Time.d.strftime("%M"))
        return Time.d.strftime("%H") + ":" + Time.d.strftime("%M")

