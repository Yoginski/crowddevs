import json

from config import CHANNEL_ID, RESOURCES_DIR
from utils import InlineMarkupBuilder


current_message_index = 0;
messages = []
with open("{}/messages.txt".format(RESOURCES_DIR)) as f:
    contents = f.read()
    messages = [m.strip() for m in contents.split("---")]

def stub_message_job(bot, updater):
    global current_message_index

    current_message_index = (current_message_index + 1) % len(messages)
    donate_button_callback_data = { "donation_id": current_message_index }
    button_markup = InlineMarkupBuilder()\
        .add_button("Пожертвовать!", json.dumps(donate_button_callback_data))\
        .to_markup()
    print(button_markup)
    bot.send_message(text=messages[current_message_index], chat_id=CHANNEL_ID, reply_markup=button_markup)
