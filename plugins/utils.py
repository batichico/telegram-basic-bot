from config import *

def create_keyboard(dict_buttons):
  
  keyboard = types.InlineKeyboardMarkup()
  lst_inline_buttons = []
  for key, value in dict_buttons.items():
    lst_inline_buttons.append(types.InlineKeyboardButton(value, callback_data=key))
  keyboard.add(*lst_inline_buttons)

  return keyboard