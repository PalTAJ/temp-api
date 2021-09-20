# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib
#
# def send_mail(to,subject,content):
#     msg = MIMEMultipart()
#     message = content
#     ###setup the parameters of the message
#     password = "E7kFKYjVnX"
#     msg['From'] = "metaboliticsdb@gmail.com"
#     #
#     # password = ""
#     # msg['From'] = "tajsaleh96@gmail.com"
#     msg['To'] = to
#     msg['Subject'] = subject
#
#     msg.attach(MIMEText(message, 'plain'))
#     server = smtplib.SMTP('smtp.gmail.com: 25')
#     server.starttls()
#     server.login(msg['From'], password)
#     server.sendmail(msg['From'], msg['To'], msg.as_string())
#     server.quit()
#
# # send_mail("tajothman@std.sehir.edu.tr",'test','test')
#

# from flask_mail import Message

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(to,subject,content):
    message = Mail(
        from_email='metaboliticsdb@gmail.com',
        to_emails= to,
        subject= subject,
        html_content= content)
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e)
