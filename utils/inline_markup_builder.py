from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class InlineMarkupBuilder:
    def __init__(self):
        self.buttons = []
        self.current_line = -1
        self.new_line()

    def add_button(self, button_text, callback_data):
        button = InlineKeyboardButton(button_text, callback_data=callback_data)
        self.buttons[self.current_line].append(button)
        return self

    def new_line(self):
        self.current_line += 1
        self.buttons.append([])
        return self

    def to_markup(self):
        return InlineKeyboardMarkup(self.buttons)
