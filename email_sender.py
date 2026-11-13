import os
import smtplib

from dotenv import load_dotenv
from email.message import EmailMessage


load_dotenv()


sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")


def send_email(receiver_email, candidate_name):

    message = EmailMessage()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Walk-in Interview Confirmation"


    body = f"""
Hello {candidate_name},

Congratulations!

Your resume has been shortlisted for our walk-in interview.

Please attend the interview on the scheduled date.

Regards,
HR Team
"""

    message.set_content(body)


    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.send_message(message)


    print(
        "Mail sent to:",
        receiver_email
    )