import telebot

TOKEN = "6422417252:AAE_F0p48ohgHKGE_LU-DG6uZNY7ieMemDM"
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(content_types=['text'])
def new_message(message):
    print(f"{message.from_user.username}: {message.text}")
    bot.send_message(message.chat.id, message.text)


print("Бот запущен")
bot.infinity_polling()