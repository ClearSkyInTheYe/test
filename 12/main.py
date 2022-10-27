import telebot
from PIL import Image, ImageDraw

bot = telebot.TeleBot('5488116829:AAEKn4npjxX7JGcHOKV3QJXePp2H4My4-Ew')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
   if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

@bot.message_handler(content_types=['photo'])
def img_hand(message):
   bot.send_message(message.from_user.id, "nice")

bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
   pass