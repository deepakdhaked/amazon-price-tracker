import os
import smtplib
import ssl
from scraper import URL
from dotenv import load_dotenv


def send_secure_email(sender_email, sender_password, receiver_email, subject, body):
    # Configure the SMTP server settings
    smtp_server = 'smtp.gmail.com'
    port = 587  # For SSL use port 465, for TLS use port 587

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        # Upgrade the connection to a secure TLS connection
        server.starttls(context=context)

        # Login to your account
        server.login(sender_email, sender_password)

        # Create the email message
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Email sent successfully!")

        # Close the connection to the server
        server.quit()


# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
receiver_email = os.getenv("RECIPIENT_EMAIL")

subject = 'Price Fall Down!!!'
body = f'Check The Amazom Link : {URL}'


