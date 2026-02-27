import requests
from configure import PUSHOVER_USER_TOKEN, PUSHOVER_API_TOKEN

def sendSms(deals: list[dict]):
    if not deals:
        body = "🎮 PS Store Deals: No wishlist games on sale today."
    else:
        top   = deals[:3]
        lines = ["🎮 PS Store Deals Today:"]
        for d in top:
            lines.append(
                f"• {d.get('name', '?')} — {d.get('sale_price', '?')} ({d.get('discount', '?')}% OFF)"
            )
        if len(deals) > 3:
            lines.append(f"...and {len(deals) - 3} more. Check your email!")
        body = "\n".join(lines)

    try:
        resp = requests.post("https://api.pushover.net/1/messages.json", data={
            "token":   PUSHOVER_API_TOKEN,
            "user":    PUSHOVER_USER_TOKEN,
            "title":   "PlayStation Store Deals",
            "message": body,
            "url":     deals[0].get("url", "") if deals else "",
            "url_title": "View on DekuDeals" if deals else "",
            "sound":   "cashregister"
        })
        resp.raise_for_status()
        print(f"[✓] Pushover notification sent.")
    except Exception as e:
        print(f"[ERROR] Pushover failed: {e}")