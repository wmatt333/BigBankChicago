import requests
import time
check = "99.0%"
approval = "10.3%"
discord_message = "hi"
json_url = 'https://projects.fivethirtyeight.com/polls/favorability/donald-trump/polling-average.json'
while 1 > 0:
    try:
        response = requests.get(json_url)
        response.raise_for_status()
        data = response.json()
        if data:
            approve_rating = data[0]["pct_estimate"]
            approval = round(float(approve_rating),1)
            discord_message = {
                "content": f"**538 Trump Approval Rating**\n**Approval**: {approval}%"
            }
        else:
            print("No data found.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    if check != approval:
        check = approval
        discord_webhook_url = 'https://discord.com/api/webhooks/1319521502206496788/1wUM-BPiRkULRCbDcjAeryimuhO07ZTjSxmfHz0exdrMqJdM_gmSMuqeKTQfIC1HMayr'
        try:
            webhook_response = requests.post(discord_webhook_url, json=discord_message)
            webhook_response.raise_for_status()
            print(f"Data sent to Discord webhook successfully: {webhook_response.status_code}")
        except requests.RequestException as e:
            print(f"Error sending data to Discord webhook: {e}")
