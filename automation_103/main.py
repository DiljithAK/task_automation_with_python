import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

try:
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.starttls()

    smtp.login('diljithak07@gmail.com', 'rdhflbmzvjfopsmd')

    # message = "Hello world from Brevo SMTP Server"
    # subject = "Your Subject Here"
    # body = "Hello world from Brevo SMTP Server"
    # message = f"Subject: {subject}\n\n{body}"

    msg = MIMEMultipart('alternative')
    msg['From'] = formataddr(('Diljith A K', 'diljithak07@gmail.com'))
    msg['To'] = 'diljithak23@gmail.com'
    msg['Subject'] = "Test Subject From Dev"

    with open('automation_103/email_content.html', 'r') as f:
        html = f.read()
        content = MIMEText(html, 'html')
        msg.attach(content)

    # email_list = ['diljithak23@gmail.com', 'diljithak1@gmail.com', 'diljith.gitrepo@gmail.com', 'dilsha.ajay.marriagealbum@gmail.com']
    smtp.sendmail('diljithak07@gmail.com', 'diljithak23@gmail.com', msg.as_string())

    smtp.quit()
except Exception as e:
    print(e)