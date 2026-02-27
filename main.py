from datetime import datetime
from fetch import fetchPsDeals
from dealFormatter import formatDeals
from emailSender import sendEmail
from smsSender import send_sms

def main():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Starting PS Deals Notifier...")

    deals = fetch_ps_deals()
    plain_text, html = format_deals(deals)

    send_email(plain_text, html, len(deals))
    send_sms(deals)

    print("[✓] Done.\n")


if __name__ == "__main__":
    main()
