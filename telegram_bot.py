import requests

def send_message(message):
    with open("text 3.txt", "r") as f:
        token = f.read().strip()

    chat_id = "YOUR_CHAT_ID"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload)

send_message("🚀 البوت شغّال وتم الإرسال بنجاح!")
