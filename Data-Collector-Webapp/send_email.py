# Sends an email to the user with the
# average height from the database.
from email.mine.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    from_email = "user@gmail.com"  # Email account you want to send emails from
    from_pass = "email_pass"  # Account's password
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>cm.\n" % height
    message += "Average Height is <strong>%s</strong>cm " % average_height
    message += "out of <strong>%s</strong> people." % count

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    # This is specifically for GMAIL accounts
    gmail_acc = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_acc.ehlo()
    gmail_acc.starttls()
    gmail_acc.login(from_email, from_pass)
    gmail_acc.send_message(msg)
