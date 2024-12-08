import requests
import time
from datetime import datetime
check = float(99.0)
while 1 > 0:
    time_now = time.time()
    current_time = time_now
    json_url = 'https://projects.fivethirtyeight.com/biden-approval-rating/approval.json'
    try:
        response = requests.get(json_url)
        response.raise_for_status()
        data = response.json()
        if data:
            approve_rating = data[0]["approve_estimate"]
            approval = round(float(approve_rating),1)
            discord_message = {
                "content": f"**538 Biden Approval Rating**\n**Approval**: {approval}%**\n**Time**: {current_time}"
            }
        else:
            print("No data found.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    if check != approval:
        check = approval
        discord_webhook_url = 'https://discord.com/api/webhooks/1310063557567582290/VN9kFcM0WfZvEmGzoJkKuAWgZIKhOWOQ_q11E_GG-NmJW59HQlSXgOl12wa3SqhlEEs7'
        try:
            webhook_response = requests.post(discord_webhook_url, json=discord_message)
            webhook_response.raise_for_status()
            print(f"Data sent to Discord webhook successfully: {webhook_response.status_code}")
        except requests.RequestException as e:
            print(f"Error sending data to Discord webhook: {e}")
