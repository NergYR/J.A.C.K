import smtplib
import json
import base64
import pyttsx3 as tts 
import win32com.client
from win32com.client import Dispatch
from functions import date

outlook = win32com.client.Dispatch("Outlook.Application")


config_file = "C:/Users/energ/Desktop/Code/Python/J.A.C.K/config.json"

user = json.load(open(config_file))['outlook_user']
password = json.load(open(config_file))['outlook_password']
password = base64.b64decode(password)
# avcdwnwlcjhkfsvr
#password_encode = "YXZjZHdud2xjamhrZnN2cg=="
#password_decode = base64.b64decode(password_encode)


class TTS:
    engine = tts.init()
    engine.runAndWait()


class Mail:
    
    
    def sendMail(object, to, message):
        body = 'Subject:  '+ object +'  \n\n\n' + message 
        try:
            server = smtplib.SMTP('smtp-mail.outlook.com', 587)
            print(password.decode())
            print(user)
            print(to)
            print(body)
            server.starttls()
            server.login(user, password.decode())
            server.sendmail(user, to, body)
            server.quit()
        except:
            print("Error: unable to send email")
            return False
        return True


class Calendar:
    def sendMeeting(start, subject, duration, location="none"):
        '''
        start format : yyyy-MM-dd hh:mm \n
        subject : string \n
        duration : in minute, integer \n
        location : string \n  
        
        '''
        

        
        appt = outlook.CreateItem(1) # AppointmentItem
        appt.Start = start # yyyy-MM-dd hh:mm
        appt.Subject = subject #
        appt.Duration = duration # In minutes (60 Minutes)
        appt.Location = location

        appt.Save()
        appt.Send()