import json
import logging
from enum import Enum
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class Command(Enum):

    GO_TO_MAIN = 1
    CHOOSE_PAYMENT_SYSTEM = 2
    CHOOSE_SUM = 3


class InlineMarkupBuilder:

    def __init__(self):
        self.buttons = []
        self.current_line = -1
        self.new_line()

    def add_callback_button(self, button_text, callback_data):
        button = InlineKeyboardButton(button_text, callback_data=callback_data)
        self.buttons[self.current_line].append(button)
        return self

    def add_url_button(self, button_text, url):
        button = InlineKeyboardButton(button_text, url=url)
        self.buttons[self.current_line].append(button)
        return self

    def new_line(self):
        self.current_line += 1
        self.buttons.append([])
        return self

    def to_markup(self):
        return InlineKeyboardMarkup(self.buttons)

    def build_initial_markup(donation_id):
        return InlineMarkupBuilder()\
            .add_callback_button("Пожертвовать", json.dumps({"id": donation_id, "cmd": "to_main"}))\
            .to_markup()

    def build_main_markup(donation):
        donation_id = donation.donation_id
        payment_url = donation.make_payment_url()
        builder = InlineMarkupBuilder()\
            .add_callback_button("Выбрать платежку", json.dumps({"id": donation_id, "cmd": "to_payment"}))\
            .add_callback_button("Выбрать сумму", json.dumps({"id": donation_id, "cmd": "to_sum"}))
        if payment_url is not None:
            logging.info("Sending payment url for donation id {}".format(donation_id))
            builder.new_line().add_url_button("Оплатить!", url=payment_url)

        return builder.to_markup()

    def build_payment_markup(donation_id):
        return InlineMarkupBuilder()\
            .add_callback_button("Мобильник", json.dumps({"id": donation_id, "cmd": "set_payment", "v": "mobilnik"}))\
            .new_line()\
            .add_callback_button("Элсом", json.dumps({"id": donation_id, "cmd": "set_payment", "v": "elsom"}))\
            .new_line()\
            .add_callback_button("Назад!", json.dumps({"id": donation_id, "cmd": "to_main"}))\
            .to_markup()

    def build_sum_markup(donation_id):
        return InlineMarkupBuilder()\
            .add_callback_button("100", json.dumps({"id": donation_id, "cmd": "set_sum", "v": "100"}))\
            .new_line()\
            .add_callback_button("200", json.dumps({"id": donation_id, "cmd": "set_sum", "v": "200"}))\
            .new_line()\
            .add_callback_button("Назад!", json.dumps({"id": donation_id, "cmd": "to_main"}))\
            .to_markup()
