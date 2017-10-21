import json

from config import CHANNEL_ID, RESOURCES_DIR
from utils import InlineMarkupBuilder, Donation


current_message_index = 0;
messages = []
with open("{}/messages.txt".format(RESOURCES_DIR)) as f:
    contents = f.read()
    messages = [m.strip() for m in contents.split("---")]

def stub_message_job(bot, updater):
    global current_message_index

    current_message_index = (current_message_index + 1) % len(messages)
    button_markup = InlineMarkupBuilder.build_initial_markup(current_message_index)
    bot.send_message(text=messages[current_message_index], chat_id=CHANNEL_ID, reply_markup=button_markup)
