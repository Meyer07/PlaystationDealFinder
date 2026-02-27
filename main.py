from datetime import datetime
from fetch import fetchPsDeals
from dealFormatter import formatDeals
from emailSender import sendEmail
from smsSender import sendSms
from wishlistFilter import filterWishlistDeals
from configure import WISHLIST

def main():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Starting PS Deals Notifier...")

    all_deals = fetchPsDeals()

    if WISHLIST:
        deals, not_on_sale = filterWishlistDeals(all_deals, WISHLIST)
        print(f"[✓] {len(deals)} wishlist games on sale, {len(not_on_sale)} not on sale.")
        if not_on_sale:
            print(f"[!] Not on sale: {', '.join(not_on_sale)}")
    else:
        deals = all_deals  # if wishlist is empty, send all deals

    plain_text, html = formatDeals(deals)
    sendEmail(plain_text, html, len(deals))
    sendSms(deals)

    print("[✓] Done.\n")

if __name__ == "__main__":
    main()