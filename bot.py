import os
import re
import json
import requests
from flask import Flask, request

TOKEN = os.getenv("API_TOKEN")
WEBHOOK_URL = f"https://rteyrty-haic.onrender.com/webhook/{TOKEN}"

# Патерни для пошуку спаму
SPAM_PATTERNS = [
    (r"@\w+", "згадка користувача"),
    (r"http[s]?://|www\.\w+", "посилання"),
    (r"t\.me/", "посилання на Telegram"),
    (r"(продаж|купівля)", "ключове слово: продаж/купівля"),
]

def find_spam_reason(text):
    text = text.lower()
    for pattern, reason in SPAM_PATTERNS:
        if re.search(pattern, text):
            return reason
    return None

def delete_message(chat_id, message_id):
    url = f"https://api.telegram.org/bot{TOKEN}/deleteMessage"
    payload = {'chat_id': chat_id, 'message_id': message_id}
    try:
        resp = requests.post(url, data=payload)
        return resp.ok
    except Exception as e:
        print("Delete error:", e)
        return False

def send_warn(chat_id, user, reason):
    msg = f"Повідомлення від {user} було видалено. Причина: {reason}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {'chat_id': chat_id, 'text': msg}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Send warn error:", e)

app = Flask(__name__)

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    try:
        update = request.get_json(force=True)
        if 'message' in update:
            msg = update['message']
            chat_id = msg['chat']['id']
            msg_id = msg['message_id']
            user = msg['from']
            # Формуємо згадку
            if "username" in user:
                mention = f"@{user['username']}"
            else:
                mention = user.get('first_name', 'Користувач')
            text = msg.get('text', '') or msg.get('caption', '')
            reason = find_spam_reason(text)
            if reason:
                delete_message(chat_id, msg_id)
                send_warn(chat_id, mention, reason)
        return "ok", 200
    except Exception as e:
        print("Error:", e)
        return "ok", 200

@app.route('/', methods=['GET'])
def index():
    return "AntiSpam Bot працює", 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
