import smtplib
from email.message import EmailMessage
from credentials import USERNAME, PASSWORD

email = EmailMessage()
email['from'] = 'Yash Kanani'
email['to'] = 'ykanani0@gmail.com'
email['subject'] = 'test email'

email.set_content('I am a test email sent via python script.')

# setting up smtp server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # smtp handshake initiate
    smtp.ehlo()
    # smtp tls secure connection establish
    smtp.starttls()
    # smtp login into email account
    smtp.login(USERNAME, PASSWORD)
    # smtp sending email
    smtp.send_message(email)
    print('email sent!')