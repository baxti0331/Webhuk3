import os
from flask import Flask, request
import telebot
from werkzeug.middleware.proxy_fix import ProxyFix

API_TOKEN = os.environ.get("API_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/api/bot", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.get_data().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    web_app_info = telebot.types.WebAppInfo(url="https://x-0-pi.vercel.app/")
    button = telebot.types.InlineKeyboardButton(text="PLAY🕹️", web_app=web_app_info)
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Нажми кнопку чтобы открыть приложение.", reply_markup=markup)

@app.route("/ping")
def ping():
    # Этот маршрут нужен для пинга сервера (чтобы он не засыпал)
    return "pong", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
