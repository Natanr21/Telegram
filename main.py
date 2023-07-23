import telebot

token = "6304383184:AAHoeMxlOOFGXtlEDPwvKiYTIYPd-aXeV-o"
chat_id = 5801817823

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,"Olá!")

print("OK")
bot.polling(non_stop=True)

#5801817823