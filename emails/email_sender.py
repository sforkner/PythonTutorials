import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'sam x dummy'
email['to'] = 'forkner@epbfi.com'
email['subject'] = 'You May be A Wienner!'

email.set_content('I am a Python Moron!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('samxdummy@gmail.com', 'B1gTr0ut!')
    smtp.send_message(email)

print("All Done")