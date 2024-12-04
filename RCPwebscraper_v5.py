import requests
import time
from datetime import datetime
check = float(99.0)
while 1 > 0:
    json_url = 'https://www.realclearpolitics.com/poll/race/7320/polling_data.json'
    try:
        response = requests.get(json_url)
        response.raise_for_status()
        data = response.json()
        if data:
            approve_rating = data["poll"][0]["candidate"][0]["value"]
            approval = round(float(approve_rating),1)
            discord_message = {
                "content": f"**RCP Biden Approval Rating**\n**Approval**: {approval}%"
            }
        else:
            print("No data found.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    if check != approval:
        check = approval
        discord_webhook_url = 'https://discord.com/api/webhooks/1310074976619069460/MpO-GdcE4k8cg22jHipfkvGwnBTVNA1N4q2gP_Ra50msvUhuwPtVi3yOVymxgXJlu6xw'
        try:
            webhook_response = requests.post(discord_webhook_url, json=discord_message)
            webhook_response.raise_for_status()
            print(f"Data sent to Discord webhook successfully: {webhook_response.status_code}")
        except requests.RequestException as e:
            print(f"Error sending data to Discord webhook: {e}")
