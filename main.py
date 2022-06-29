from time import timezone
from functions import date 
from functions import outlook
from functions import google

#google.Mail.sendMail("Test", "xzeystape@gmail.com", "This is a test")



outlook.Calendar.sendMeeting(date.dt.datetime.now(), "Test", 10, "Here")

# date.Time.sayDateTime()