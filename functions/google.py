from calendar import calendar
import smtplib
import json
import base64
import pyttsx3 as tts 
from functions import date

from datetime import datetime, timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = 'C:/Users/energ/Desktop/Code/Python/J.A.C.K/credentials.json'


config_file = "C:/Users/energ/Desktop/Code/Python/J.A.C.K/config.json"

user = json.load(open(config_file))['google_user']
password = json.load(open(config_file))['google_password']
password = base64.b64decode(password)
#ttueyekzcyncwdgx


class Mail:
    
    
    def sendMail(object, to, message):
        body = 'Subject:  '+ object +'  \n\n\n' + message 
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
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
    def get_calendar_service():
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)
        return service
    def addEvent(Stime, Etime, name, description="none", location="Endorium Group"):
        service = Calendar.get_calendar_service()
        timezone = date.timezone#"Europe/Paris"#
        """
        Add new event in Google Calendar 
        addEvent(Stime["YYYY-MM-DDTHH:MM:SS"],Etime["YYYY-MM-DDTHH:MM:SS"],name,description, (location))

        """ 

        event = {
        'summary': name,
        'location': location,
        'description': description,
        'start': {
            'dateTime': Stime,
            'timeZone': str(timezone),
        },
        'end': {
            'dateTime': Etime,
            'timeZone': str(timezone),
        },


        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

        event = service.events().insert(calendarId='xzeystape@gmail.com', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        print("Event added to Google Calendar %s" % (event.get('eventId')))
        
        
        
    def getEvents():
        '''
        List 10 Events from Google Calendar
        '''
        service = Calendar.get_calendar_service()
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting List o 10 events')
        events_result = service.events().list(
            calendarId='xzeystape@gmail.com', timeMin=now,
            maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            
            
    def updateEvents(eventID, name, Etime, Stime, description="none"):
        '''
        ## Update an event in Google Calendar \n
        Usage : ``updateEvents(eventID, name, Etime, Stime, description, location)`` \n
        ``id`` = eventID \n
        ``name`` = name of the event (string) \n
        ``Etime`` = End Time => YYYY-MM-DDTHH:MM:SS \n
        ``Stime`` = Start Time => YYYY-MM-DDTHH:MM:SS \n
        ``description`` = description (optional) (string) \n
        ``location`` = location (optional) (string) \n
        '''
        service = Calendar.get_calendar_service()
        timezone = date.timezone#"Europe/Paris"#


        event_result = service.events().update(
          calendarId='xzeystape@gmail.com',
          eventId= eventID,
          body={
           "summary": name,
           "description": description,
           "start": {"dateTime": Stime, "timeZone": str(timezone)},
           "end": {"dateTime": Etime, "timeZone": str(timezone)},
           },
        ).execute()

        print("updated event")
        print("id: ", event_result['id'])
        print("summary: ", event_result['summary'])
        print("starts at: ", event_result['start']['dateTime'])
        print("ends at: ", event_result['end']['dateTime'])


