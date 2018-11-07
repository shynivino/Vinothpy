import smtplib

from_mail = 'doddahulugappa@gmail.com'
password = '9945208358'
to_mail = 'shankaragouda.g@gmail.com'
gmail_server = 'smtp.gmail.com'
gmail_port = 587
mail_body = "Hi Dear, Hope you are doing well"
subject = "Test"
email_text = """  
From: %s  
To: %s  
Subject: %s

 %s
""" % (from_mail,to_mail, subject, mail_body)
try:
    mail_server = smtplib.SMTP(gmail_server,gmail_port)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(from_mail,password)
    mail_server.sendmail(from_mail,to_mail,email_text)
    print("Mail has been sent")
except Exception as E:
    print("Something went wrong:",E)
finally:
    mail_server.close()


