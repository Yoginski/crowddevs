import json
import logging
from utils import InlineMarkupBuilder, Donation


def callback_query_handler(bot, update):
    
    json_data = json.loads(update.callback_query.data)
    user_id = update.callback_query.from_user.id
    donation_id = json_data["id"]
    cmd = json_data.get("cmd", "to_initial")
    markup = None
    logging.info("Received callback command {} from user {} for donation id {}".format(cmd, user_id, donation_id))
    if cmd == "to_initial":
        markup = InlineMarkupBuilder.build_initial_markup(donation_id)
    elif cmd == "to_payment":
        markup = InlineMarkupBuilder.build_payment_markup(donation_id)
    elif cmd == "to_sum":
        markup = InlineMarkupBuilder.build_sum_markup(donation_id)
    elif cmd == "to_main":
        session = Donation.get_session(user_id, donation_id)
        markup = InlineMarkupBuilder.build_main_markup(session)
    elif cmd == "set_payment":
        session = Donation.get_session(user_id, donation_id)
        session.payment_system = json_data["v"]
        markup = InlineMarkupBuilder.build_main_markup(session)
    elif cmd == "set_sum":
        session = Donation.get_session(user_id, donation_id)
        session.sum = json_data["v"]
        markup = InlineMarkupBuilder.build_main_markup(session)
#    update.callback_query.answer("HI")
    update.callback_query.message.edit_reply_markup(reply_markup=markup)
