import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from jinja2 import Template

# Email credentials and server configuration
email = 'testsmtp@gmail.com'  # Your SMTP email address
password = 'your-smtp-password'  # Your SMTP password

# List of recipient email addresses
recipients = [
    {'email': 'alan1@gmail.com', 'name': 'Alan'},
    {'email': 'nanesh2@gmail.com', 'name': 'Nanesh'},
    {'email': 'sanal3@gmail.com', 'name': 'Sanal'},
    {'email': 'adil4@gmail.com', 'name': 'Adil'},
    {'email': 'savad5@gmail.com', 'name': 'Savad'}
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

        # Load email content
        template_str = load_email_template(EMAIL_TEMPLATE)
        if not template_str:
            raise Exception('Failed to load email content.')
        template = Template(template_str)

        for recipient in recipients:
            name = recipient['name']
            recipient_email = recipient['email']

            # Create the email
            msg = MIMEMultipart('alternative')
            msg['From'] = formataddr(('Your Name', email))
            msg['To'] = recipient_email
            msg['Subject'] = "My Email Subject"

            # Render HTML content with recipient full name
            html_content = template.render(name=name)
            msg.attach(MIMEText(html_content, 'html'))

            # Send the email
            smtp.sendmail(email, recipient_email, msg.as_string())
        
        # Quit the SMTP server
        smtp.quit()
        print('Emails sent successfully.')
    except Exception as e:
        print(f"Failed to send email: {e}")