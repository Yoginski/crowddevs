import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from config import BOT_TOKEN
from handlers import donate_command_handler, callback_query_handler

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

updater = Updater(BOT_TOKEN)

updater.dispatcher.add_handler(CommandHandler('donate', donate_command_handler))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_query_handler))

updater.start_polling()
updater.idle()
