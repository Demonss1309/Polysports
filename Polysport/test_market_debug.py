import json
import requests

url = "https://gamma-api.polymarket.com/events"
params = {
    "tag": "lol",
    "limit": 10,
    "closed": False,
    "active": True
}

print("Fetching LOL markets from Polymarket...")
response = requests.get(url, params=params, timeout=15)

print("Status code:", response.status_code)

if response.status_code != 200:
    print("Failed to fetch data")
    exit()

events = response.json()
print(f"Total events received: {len(events)}\n")

market_count = 0

for event in events:
    markets = event.get("markets", [])
    for market in markets:
        question = market.get("question", "")
        slug = market.get("slug")

        outcomes = json.loads(market.get("outcomes", "[]"))
        prices = json.loads(market.get("outcomePrices", "[]"))
        token_ids = json.loads(market.get("clobTokenIds", "[]"))

        if len(outcomes) < 2:
            continue

        price0 = float(prices[0]) * 100
        price1 = float(prices[1]) * 100

        print("=" * 60)
        print(f"Question: {question}")
        print(f"Slug: {slug}")

        print(f"\nOutcome 0: {outcomes[0]}")
        print(f"  Price: {price0:.1f}¢")
        print(f"  Token ID: {token_ids[0]}")

        print(f"\nOutcome 1: {outcomes[1]}")
        print(f"  Price: {price1:.1f}¢")
        print(f"  Token ID: {token_ids[1]}")

        # Determine strong vs weak team
        if price0 > price1:
            strong = outcomes[0]
            strong_price = price0
            weak = outcomes[1]
            weak_price = price1
        else:
            strong = outcomes[1]
            strong_price = price1
            weak = outcomes[0]
            weak_price = price0

        print(f"\nStrong team: {strong} @ {strong_price:.1f}¢")
        print(f"Weak team:   {weak} @ {weak_price:.1f}¢")

        market_count += 1

        if market_count >= 5:
            print("\nShown 5 markets only (limit reached).")
            exit()

print("\nNo markets found.")
