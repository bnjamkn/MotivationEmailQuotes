import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path


from dotenv import load_dotenv  # pip install python-dotenv

# Use the mail services server information for SMTP, here outlook (hotmail) is used
PORT = 587
EMAIL_SERVER = "smtp-mail.outlook.com"

# Load the environment variables
current_dir = Path(__file__).resolve(
).parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables from env file
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(subject, receiver_email, name, day, daysLeft, quote, author):
    # Create the base text message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(
        ("whatever you want the recipient to read you as", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    # Replace "your name here with" desired name
    msg.set_content(
        f"""\
            Hello  {name}, 

            Today is day {day} of daily quotes, and there are {daysLeft} more to come. Below you will find your daily qoute. 

            {quote}
            - {author}

            All the best, 

            Your name here  

            """
    )

    # HMTL version of the mail, the email will usually be read with this formating if the mail-reader from the recipient allows it. (which most do)

    msg.add_alternative(
        f"""\
        <html>
        <meta http-equiv="Content-Type" content="text/html" charset="utf-8"/>
        <body>
            <p>Hello {name}, </p>
            <p>Today is day <strong>{day}</strong> of daily quotes, and there are <strong>{daysLeft}</strong> more to come. Below you will find your daily qoute.</p>
            <p></p>
            <p>"<i>{quote}</i>" <br> - {author}</p>
            <p></p>
            <p>All the best,</p>
            <p>Your name here</p>
        </body>
        </html>
        """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())
