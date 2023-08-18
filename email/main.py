import smtplib
import ssl
from email.message import EmailMessage

sender = 'samoracuteedancletus@gmail.com'
subject = 'Urgent Information'
body = 'Dear valued customer kindly be advised that we have been authorized by the government to close your dormant account with immediate effect.'
password = input('Enter password: ')
receiver = 'officialsamcletus@gmail.com'

message = EmailMessage()
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())

print("Email Sent!")
