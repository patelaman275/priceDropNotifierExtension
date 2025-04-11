import time
from storage import load_data, save_data
from scraper import get_price
from utils import notify
import schedule

def monitor_prices():
    data = load_data()
    updated = False

    for url, old_price in data.items():
        current_price = get_price(url)
        if current_price is None:
            continue

        if current_price < old_price:
            notify("Price Dropped!", f"New Price: ₹{current_price}")
            data[url] = current_price
            updated = True

    if updated:
        save_data(data)

def run_monitor():
    schedule.every(1).hour.do(monitor_prices)
    print("Background price monitor running...")

    while True:
        schedule.run_pending()
        time.sleep(60)
