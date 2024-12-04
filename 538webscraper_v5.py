import requests
import time
from datetime import datetime
check = float(99.9)
while 1 > 0:
    json_url = 'https://projects.fivethirtyeight.com/biden-approval-rating/approval.json'
    try:
        response = requests.get(json_url)
        response.raise_for_status()
        data = response.json()
        if data:
            data.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
            most_recent_entry = data[-1]
            approve_estimate = most_recent_entry.get('approve_estimate')
            approval = round(float(approve_estimate),1)
            discord_message = {
                "content": f"**538 Biden Approval Rating**\n**Approval**: {approval}%"
            }
        else:
            print("No data found.")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    if check != approve_estimate:
        check = approve_estimate
        discord_webhook_url = 'https://discord.com/api/webhooks/1310063557567582290/VN9kFcM0WfZvEmGzoJkKuAWgZIKhOWOQ_q11E_GG-NmJW59HQlSXgOl12wa3SqhlEEs7'
        try:
            webhook_response = requests.post(discord_webhook_url, json=discord_message)
            webhook_response.raise_for_status()
            print(f"Data sent to Discord webhook successfully: {webhook_response.status_code}")
        except requests.RequestException as e:
            print(f"Error sending data to Discord webhook: {e}")
    time.sleep(0.1)

