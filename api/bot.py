import telebot
from flask import Flask, request

API_TOKEN = "8116822393:AAHjGpU3xTNhaNvDnteSQu0aSHuq9pmFtPs"
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route("/api/bot", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.get_json())
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    web_app_info = telebot.types.WebAppInfo(url="https://x-0-pi.vercel.app/")
    button = telebot.types.InlineKeyboardButton(text="PLAY🕹️", web_app=web_app_info)
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Нажми Кнопку чтобы открыть приложение.", reply_markup=markup)
