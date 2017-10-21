import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def donate_command_handler(bot, update):
    json_data = {
        "command": "donate",
        "donation_id": "123"
    }
    hello_button_1 = InlineKeyboardButton("zhopa1", callback_data=json.dumps(json_data))
    hello_button_2 = InlineKeyboardButton("zhopa2", url="http://google.com")
    button_markup = InlineKeyboardMarkup([[hello_button_1, hello_button_2]])

    update.message.reply_text('Hello World!', reply_markup=button_markup)
