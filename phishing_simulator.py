import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def send_phishing_simulation_email(sender_email, receiver_email, subject, body):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"  # Example using Gmail's SMTP server
    smtp_port = 587  # Port for TLS

    # Get the sender's email password securely
    password = getpass.getpass("Enter your email password: ")

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure
        server.login(sender_email, password)  # Log in to the email account

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Phishing simulation email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()  # Close the connection

if __name__ == "__main__":
    # Email details
    sender_email = "kaniskaroy333@gmail.com"  # Replace with your email
    receiver_email = "cyberbunny137@gmail.com"  # Replace with the target email
    subject = "Urgent: Verify Your Account Now"
    body = """
    Dear User,

    We have detected unusual activity on your account. To secure your account, please verify your details by clicking the link below:

    http://fake-phishing-link.com

    If you do not take action within 24 hours, your account will be suspended.

    Sincerely,
    The Security Team
    """

    # Send the phishing simulation email
    send_phishing_simulation_email(sender_email, receiver_email, subject, body)