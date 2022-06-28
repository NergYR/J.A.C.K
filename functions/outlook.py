import smtplib
import json
import base64


config_file = "C:/Users/energ/Desktop/Code/Python/J.A.C.K/config.json"

user = json.load(open(config_file))['outlook_user']
password = json.load(open(config_file))['outlook_password']
password = base64.b64decode(password)
# avcdwnwlcjhkfsvr
#password_encode = "YXZjZHdud2xjamhrZnN2cg=="
#password_decode = base64.b64decode(password_encode)

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


    