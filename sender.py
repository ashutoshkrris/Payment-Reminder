import requests

import os

PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")
TOKEN = os.environ.get('WHATSAPP_TOKEN')


def send_whatsapp_message(title, amount, payment_link, to):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}'
        }
        preview_url = False
        reminder = f"⚠️PAYMENT REMINDER⚠️\n\nHey Ashutosh!\nYou have a payment reminder:\n\n*{title}* : *₹ {amount}*\n\n"

        if payment_link:
            reminder += f"Payment Link: {payment_link}"
            preview_url = True

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "text",
            "text": {
                "preview_url": preview_url,
                "body": reminder
            }
        }
        response = requests.post(
            f"https://graph.facebook.com/v14.0/{PHONE_NUMBER_ID}/messages", json=data, headers=headers)
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(e)
        print("Something went wrong. Message not sent.")
