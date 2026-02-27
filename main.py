from datetime import datetime
from fetch import fetchPsDeals
from dealFormatter import formatDeals
from emailSender import sendEmail
from smsSender import sendSms

def main():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Starting PS Deals Notifier...")

    deals = fetchPsDeals()
    plain_text, html = formatDeals(deals)

    sendEmail(plain_text, html, len(deals))
    sendSms(deals)

    print("[✓] Done.\n")


if __name__ == "__main__":
    main()
