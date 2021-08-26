from  email.mime.text import MIMEText
import smtplib


def sendEmail(email, height, average_height, count):
    from_email = "twenet1212@gmail.com"
    from_password =  "GodofsoN2706"
    to_email = email

    subject="Height data"
    message = "Hey there, your height is <strong>%s</strong>. Average height of all is <strong>%s</strong> and that is calculated out <strong>%s</strong> of people" % (height, average_height, count)

    #message would be head as html text
    msg = MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail= smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)