import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from configure import ROADRUNNER_EMAIL, ROADRUNNER_PASSWORD, TO_EMAILS


def sendEmail(plain_text: str, html: str, deal_count: int):
    today   = datetime.now().strftime("%b %d, %Y")
    subject = f"🎮 PS Store Deals — {deal_count} sales today ({today})"

    msg            = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = ROADRUNNER_EMAIL
    msg["To"]      = TO_EMAILS

    msg.attach(MIMEText(plain_text, "plain"))
    msg.attach(MIMEText(html,       "html"))

    try:
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(ROADRUNNER_EMAIL, ROADRUNNER_PASSWORD)
            server.sendmail(ROADRUNNER_EMAIL, TO_EMAILS, msg.as_string())
        print(f"[✓] Email sent to {TO_EMAILS}")
    except Exception as e:
        print(f"[ERROR] Email failed: {e}")