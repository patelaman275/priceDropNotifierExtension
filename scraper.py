import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}



def resolve_redirect(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=chrome_options)
        driver.set_page_load_timeout(15)
        driver.get(url)

    
        time.sleep(3)
        resolved_url = driver.current_url
        driver.quit()
        return resolved_url
    except Exception as e:
        print(f"[ERROR] Selenium redirect failed: {e}")
        return url

def get_price_flipkart(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(3)
        price_selectors = [
            "._30jeq3._16Jk6d",   
            "._16Jk6d",           
        ]

        price_text = None
        for selector in price_selectors:
            elems = driver.find_elements("css selector", selector)
            if elems:
                price_text = elems[0].text.strip()
                break

        driver.quit()

        if price_text:
            return float(price_text.replace("₹", "").replace(",", ""))

    except Exception as e:
        print(f"[ERROR] Flipkart Selenium scraping failed: {e}")
    return None


def get_price_amazon(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        price_span = soup.find("span", class_="a-offscreen")
        if price_span:
            price_text = price_span.get_text().replace("₹", "").replace(",", "").strip()
            return float(price_text)
    except Exception as e:
        print(f"[ERROR] Amazon scraping failed: {e}")
    return None

def get_price(url):
    url = resolve_redirect(url)
    print("Resolved URL:", url)
    if "flipkart.com" in url:
        return get_price_flipkart(url)
    elif "amazon." in url:
        return get_price_amazon(url)
    return None

