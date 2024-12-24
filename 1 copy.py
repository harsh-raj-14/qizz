import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, app_password, recipient_email, subject, body):
    try:
        # Set up the MIME structure
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Use SMTP_SSL with port 465
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.send_message(message)
        
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Usage
sender_email = "stockraj0@gmail.com"
sender_password = "hrtq qvkt kteo msyb"
recipient_email = "harshraj.2222006@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python!"
send_email(sender_email, sender_password, recipient_email, subject, body)
