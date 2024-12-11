import requests
import time
from datetime import datetime
check = str(0000-00-00)
while 1 > 0:
    time_now = time.time()
    current_time = time_now
    json_url = 'https://projects.fivethirtyeight.com/biden-approval-rating/polls.json'
    try:
        response = requests.get(json_url)
        response.raise_for_status()
        data = response.json()
        if data:
            approve_rating = data[0]["created_at"]
            approval = (str(approve_rating))
            discord_message = {
                "content": f"**538 Biden Approval Rating**\n**Poll Created at: {approve_rating}**"
            }
        else:
            print("No data found.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    if check != approval:
        check = approval
        discord_webhook_url = 'https://discord.com/api/webhooks/1316163738927235082/U1hHRuLzmo0mivNDODcx_0VBYiNm81-aee3EeMBGN8-WUudRUnX3KqJ35tyzFhuw8zp7'
        try:
            webhook_response = requests.post(discord_webhook_url, json=discord_message)
            webhook_response.raise_for_status()
            print(f"Data sent to Discord webhook successfully: {webhook_response.status_code}")
        except requests.RequestException as e:
            print(f"Error sending data to Discord webhook: {e}")