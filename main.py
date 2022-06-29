from time import timezone
from functions import date 
from functions import outlook
from functions import google

#google.Mail.sendMail("Test", "xzeystape@gmail.com", "This is a test")

#google.Calendar.addEvent("2022-06-30T10:15:00", "2022-06-30T12:00:00", "Oral Bac", "Ne pas oublier, -convoc \n -carte ID \n -les livres \n -les textes", "Lycée Guillaume Budé")

google.Calendar.getEvents()

# outlook.Calendar.sendMeeting(date.dt.datetime.now(), "Test", 10, "Here")

# date.Time.sayDateTime()