import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from configure import ROADRUNNER_EMAIL, ROADRUNNER_PASSWORD, TO_EMAILS

def sendEmail(plain_text: str, html: str, deal_count: int):
    if not plain_text or not html:
        print("[!] No deals to send, skipping email.")
        return

    today   = datetime.now().strftime("%b %d, %Y")
    subject = f"🎮 PS Store Deals — {deal_count} sales today ({today})"

    # Handle both a single email string or a list of emails
    recipients = TO_EMAILS if isinstance(TO_EMAILS, list) else [TO_EMAILS]

    try:
        with smtplib.SMTP("mail.twc.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(ROADRUNNER_EMAIL, ROADRUNNER_PASSWORD)

            for recipient in recipients:
                msg            = MIMEMultipart("alternative")
                msg["Subject"] = subject
                msg["From"]    = ROADRUNNER_EMAIL
                msg["To"]      = recipient

                msg.attach(MIMEText(plain_text, "plain"))
                msg.attach(MIMEText(html,       "html"))

                server.sendmail(ROADRUNNER_EMAIL, recipient, msg.as_string())
                print(f"[✓] Email sent to {recipient}")

    except Exception as e:
        print(f"[ERROR] Email failed: {e}")