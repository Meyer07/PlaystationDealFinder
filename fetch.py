import requests
from configure import max_deals,psRegion


def fetchPsDeals() -> list[dict]:

    url=f"https://psdeals.net/api/collection/{psRegion}/deals"
    parameters={
        "sort": "discount",
        "limit" :max_deals,
        "offset":0
    }

    headers={"User-Agent": "PS-Deals-Notifier/1.0"}


    try:
        resp=requests.get(url,params=parameters,headers=headers,timeout=15)
        resp.raise_for_status()
        data=resp.json()
        deals = data.get("data", {}).get("collection", [])
        print(f"[✓] Fetched {len(deals)} deals from PSDeals.")
        return deals
    except requests.RequestException as e:
        print(f"Error in fetching deals{e}")
        return []

