import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

try:
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.starttls()

    smtp.login('diljithak07@gmail.com', 'rdhflbmzvjfopsmd')

    msg = MIMEMultipart('alternative')
    msg['From'] = formataddr(('Diljith A K', 'diljithak07@gmail.com'))
    msg['To'] = 'diljithak23@gmail.com'
    msg['Subject'] = "Test Subject From Dev"

    html = """
    <html>
    <head></head>
    <body>
        <p>Hello world from <b>Gmail SMTP Server</b></p>
        <p>This is an example email with HTML content.</p>
    </body>
    </html>
    """

    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    smtp.sendmail('diljithak07@gmail.com', 'diljithak23@gmail.com', msg.as_string())

    smtp.quit()
except Exception as e:
    print(e)