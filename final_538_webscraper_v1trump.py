from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests

chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

url = "https://projects.fivethirtyeight.com/polls/favorability/donald-trump/"
webhook_url = "https://discord.com/api/webhooks/1309721764934189146/2hWLLzBqoZC6KG7VVlTSJq0P0_xlfWR0gm0ARfxdc3RbnWIic5ntgU4QrrnrtX6Qmlg7"

service = Service('/Users/davidchan/Downloads/chromedriver')  # Update the path to your ChromeDriver
browser = webdriver.Chrome(service=service, options=chrome_options)

def get_approval_rating():
    browser.get(url)
    time.sleep(1)
    try:
        approval_element = browser.find_element(By.CSS_SELECTOR, "g.label-group")
        return approval_element.text
    except Exception as e:
        print(f"Error finding approval rating: {e}")
        return None

def send_to_discord(approval_rating):
    payload = {
        "content": f"New Trump Approval Rating: {approval_rating[28:34]}"
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print("Successfully sent to Discord!")
    else:
        print(f"Failed to send to Discord: {response.status_code} {response.text}")

try:
    last_reported_rating = None
    while True:
        current_rating = get_approval_rating()
        if current_rating and current_rating != last_reported_rating:
            print(f"Approval Rating Updated: {current_rating}")
            send_to_discord(current_rating)
            last_reported_rating = current_rating
        time.sleep(1)  # Check for updates every second
except KeyboardInterrupt:
    print("Stopped tracking.")
finally:
    browser.quit()
