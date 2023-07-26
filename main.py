import telebot

token = "6304383184:AAHoeMxlOOFGXtlEDPwvKiYTIYPd-aXeV-o"
chat_id = 5801817823

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message,"Olá!")

#@bot.message_handler(commands="Brasileirao")
#def Brasileirao(message):
 #   bot.reply_to(message, )

#@bot.message_handler(commands="Maioresodds")
#def Maioresodds(message):
 #   bot.reply_to(message, "")


print("OK")
bot.polling(non_stop=True)

#5801817823