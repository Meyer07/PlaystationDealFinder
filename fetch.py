import requests
from bs4 import BeautifulSoup
from configure import max_deals

def fetchPsDeals() -> list[dict]:
    url = "https://www.dekudeals.com/ps-deals"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")

        deals = []
        items = soup.select(".main-card")[:max_deals]

        for item in items:
            title      = item.select_one(".name")
            sale_price = item.select_one(".sale-price")
            original   = item.select_one(".original-price")
            discount   = item.select_one(".discount-badge")
            link       = item.select_one("a")

            deals.append({
                "name":          title.text.strip()      if title      else "Unknown",
                "sale_price":    sale_price.text.strip() if sale_price else "N/A",
                "regular_price": original.text.strip()   if original   else "N/A",
                "discount":      discount.text.strip().replace("%","").replace("-","") if discount else "?",
                "url":           "https://www.dekudeals.com" + link["href"] if link else "",
                "platforms":     ["PS"],
                "sale_end_date": "",
            })

        print(f"[✓] Fetched {len(deals)} deals from DekuDeals.")
        return deals

    except requests.RequestException as e:
        print(f"Error in fetching deals: {e}")
        return []