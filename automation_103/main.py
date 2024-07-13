import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

# Email credentials and server configuration
email = 'testsmtp@gmail.com'  # Your SMTP email address
password = 'your-smtp-password'  # Your SMTP password

# List of recipient email addresses
email_list = [
    'receivermail1@gmail.com',
    'receivermail2@gmail.com',
    'receivermail3@gmail.com',
    'receivermail4@gmail.com'
]

# Path to email template
EMAIL_TEMPLATE = 'automation_103/email_content.html'

# Load the email template
def load_email_template(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f'Failed to read file: {e}')

if __name__ == '__main__':
    try:
        # Set up the SMTP server
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(email, password)

        # Create the email
        msg = MIMEMultipart('alternative')
        msg['From'] = formataddr(('Your Name', email))
        msg['Subject'] = "My Email Subject"

        # Load email content
        html = load_email_template(EMAIL_TEMPLATE)
        if not html:
            raise Exception('Failed to load email content')

        msg.attach(MIMEText(html, 'html'))

        # Send the email
        smtp.sendmail(email, email_list, msg.as_string())
        
        # Quit the SMTP server
        smtp.quit()
        print('Emails sent successfully.')
    except Exception as e:
        print(f"Failed to send email: {e}")
