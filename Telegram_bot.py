import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=data)
    return response.json()

if __name__ == "__main__":
    with open("text 3.txt", "r") as file:
        token = file.read().strip()

    chat_id = "ضع_هنا_chat_id"
    message = "🚀 Hello from your GitHub bot!"
    print(send_telegram_message(token, chat_id, message))
