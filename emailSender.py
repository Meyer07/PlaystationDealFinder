import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from configure import GMAIL_EMAIL, GMAIL_PASSWORD, TO_EMAIL


def sendEmail(plain_text: str, html: str, deal_count: int):
    today   = datetime.now().strftime("%b %d, %Y")
    subject = f"🎮 PS Store Deals — {deal_count} sales today ({today})"

    msg            = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = GMAIL_EMAIL
    msg["To"]      = TO_EMAIL

    msg.attach(MIMEText(plain_text, "plain"))
    msg.attach(MIMEText(html,       "html"))

    try:
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(GMAIL_EMAIL, GMAIL_PASSWORD)
            server.sendmail(GMAIL_EMAIL, TO_EMAIL, msg.as_string())
        print(f"[✓] Email sent to {TO_EMAIL}")
    except Exception as e:
        print(f"[ERROR] Email failed: {e}")