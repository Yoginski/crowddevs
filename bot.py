import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('477027524:AAHjzfguxYlhM1KZDUUd8vW3oihd4MsKnx0')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
