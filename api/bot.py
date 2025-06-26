import os
from flask import Flask, request
import telebot
from werkzeug.middleware.proxy_fix import ProxyFix

API_TOKEN = "8116822393:AAHjGpU3xTNhaNvDnteSQu0aSHuq9pmFtPs"
WEBHOOK_URL = "https://webhuk3.vercel.app/api/bot"  # Замените на ваш URL вебхука

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/api/bot", methods=["POST"])
def webhook():
    if request.method == "POST":
        json_string = request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Method Not Allowed", 405

@bot.message_handler(commands=['start'])
def start(message):
    print(f"Получена команда /start от {message.chat.id}")  # Лог для проверки
    markup = telebot.types.InlineKeyboardMarkup()
    web_app_info = telebot.types.WebAppInfo(url="https://x-0-pi.vercel.app/")
    button = telebot.types.InlineKeyboardButton(text="PLAY🕹️", web_app=web_app_info)
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Нажми кнопку чтобы открыть приложение.", reply_markup=markup)

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    print(f"Вебхук установлен: {WEBHOOK_URL}")
    # В локальной разработке можно запустить сервер так:
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))