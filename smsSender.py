from twilio.rest import Client
from configure import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, YOUR_PHONE_NUMBER


def sendSms(deals: list[dict]):
    if not deals:
        body = "No deals found today"
    else:
        top = deals[:3]
        lines = ["🎮 PS Store Deals Today:"]
        for d in top:
            lines.append(
                f"• {d.get('name', '?')} — {d.get('sale_price', '?')} ({d.get('discount', '?')}% OFF)"
            )
        if len(deals) > 3:
            lines.append(f"...and {len(deals) - 3} more. Check your email!")
        body = "\n".join(lines)

    try:  # <-- this should be outside and after the if/else
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=body,
            from_=TWILIO_FROM_NUMBER,
            to=YOUR_PHONE_NUMBER,
        )
        print(f"[✓] SMS sent (SID: {message.sid})")
    except Exception as e:
        print(f"[ERROR] SMS failed: {e}")