from utils import InlineMarkupBuilder


def callback_query_handler(bot, update):
    button_markup = InlineMarkupBuilder()\
        .add_button("Выбрать платежку", "choose_payment_system")\
        .add_button("Выбрать сумму", "choose_sum")\
        .new_line()\
        .add_button("Оплатить!", "pay")\
        .to_markup()
    update.callback_query.message.edit_reply_markup(reply_markup=button_markup)
