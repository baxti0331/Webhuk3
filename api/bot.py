import telebot
from flask import Flask, request

API_TOKEN = "8116822393:AAHjGpU3xTNhaNvDnteSQu0aSHuq9pmFtPs"
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route("/api/bot", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.get_json(force=True))
    if update.message:
        handle_message(update.message)
    return "OK", 200

@app.route("/api/bot", methods=["GET"])
def check():
    return "Webhook OK", 200

def handle_message(message):
    if message.text == "/start":
        markup = telebot.types.InlineKeyboardMarkup()
        web_app_info = telebot.types.WebAppInfo(url="https://x-0-pi.vercel.app/")
        button = telebot.types.InlineKeyboardButton(text="PLAY 🕹️", web_app=web_app_info)
        markup.add(button)
        
        bot.send_message(message.chat.id, "Привет! Нажми кнопку, чтобы открыть приложение.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Ты написал: {message.text}")
