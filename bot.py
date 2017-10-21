import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from config import BOT_TOKEN, STUB_SEND_INTERVAL
from handlers import donate_command_handler, callback_query_handler
from jobs import stub_message_job


logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

updater = Updater(BOT_TOKEN)

updater.dispatcher.add_handler(CommandHandler('donate', donate_command_handler))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_query_handler))

updater.job_queue.run_repeating(stub_message_job, interval=STUB_SEND_INTERVAL, first=0)

updater.start_polling()
updater.idle()
