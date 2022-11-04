import telebot
from decouple import config
from telebot import types
bot = telebot.TeleBot(config("TOKEN_BOT"))

@bot.message_handler(commands=["start", "hi"])
def get_start_massage(message):
    full_name = f"{message.from_user.username}!!!"
    text = f"Welcome {full_name}"
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=["text"])
def get_massage(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if message.text.lower()== "меню":
        text = "Выберите пожалуйства:"
        btn1 = types.InlineKeyboardButton("чай", callback_data = "tea")
        btn2 = types.InlineKeyboardButton("кофе", callback_data = "coffee")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def get_callback_data(call):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    text = ""
    if call.data == "tea":
        text = f"выберите желаемый чай внизу:"
        btn1 = types.KeyboardButton("black")
        btn2 = types.KeyboardButton("blue")
        btn3 = types.KeyboardButton("green")
        murkup.add(btn1, btn2, btn3)

    if call.data == "coffee":
        text = f"выберите желаемый кофе внизу:"
        btn1 = types.KeyboardButton("milk")
        btn2 = types.KeyboardButton("3/1")
        btn3 = types.KeyboardButton("ameri")
        btn3 = types.KeyboardButton("cap")
        murkup.add(btn1, btn2, btn3)
    bot.send_message(call.message.chat.id, text, reply_markup=murkup)





bot.polling()