import telebot

API_TOKEN = "8116822393:AAHjGpU3xTNhaNvDnteSQu0aSHuq9pmFtPs"
WEBHOOK_URL = "https://webhuk.vercel.app/api/bot"  # замени на свой домен Vercel

bot = telebot.TeleBot(API_TOKEN)
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)
print("Webhook установлен!")
