from config import *
print(f"\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@ config {config} @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n")
print(f"\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@ config.__dict__ {config.__dict__} @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n")

keyboard = types.InlineKeyboardMarkup()
keyboard.add(types.InlineKeyboardButton('Español', callback_data='es'),
             types.InlineKeyboardButton('Inglés', callback_data='en'),
             types.InlineKeyboardButton('Euskera', callback_data='eus'))

keyboard_2 = types.InlineKeyboardMarkup()
keyboard_2.add(types.InlineKeyboardButton('Spanish', callback_data='es'),
             types.InlineKeyboardButton('English', callback_data='en'),
             types.InlineKeyboardButton('Euskera', callback_data='eus'))

'''
def create_lang_keyboard(lang):
  keyboard = types.InlineKeyboardMarkup()
  buttons = responses[f"lang_{lang}_buttons"]

  lst_inline_buttons = []
  for key, value in buttons.items():
    lst_inline_buttons.append(types.InlineKeyboardButton(value, callback_data=key))
  keyboard.add(*lst_inline_buttons)

  return keyboard
'''

@bot.message_handler(commands=['lang'], func=lambda m: is_user(m.chat.id))
def lang_handler(m):
  "Función para actualizar el idioma del bot"
  cid = m.chat.id
  buttons = responses[f"lang_{lang(cid)}_buttons"]
  keyboard = create_keyboard(lang(cid), buttons)


  # keyboard = create_lang_keyboard(lang(cid))
  bot.send_message(cid, responses['lang'][lang(cid)], reply_markup=keyboard, parse_mode="Markdown")
  # bot.send_message(cid, responses['lang'][lang(cid)], reply_markup=keyboard if lang(cid) == 'es' else keyboard_2, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data in ['en', 'es','eus'])
def callback_handler(call):
    "Función para manejar el uso de los botones para cambiar el idioma"
    cid = call.message.chat.id
    mid = call.message.message_id
    language = call.data
    update_lang(cid, language)
    # keyboard = create_lang_keyboard(language)
    buttons = responses[f"lang_{language}_buttons"]
    keyboard = create_keyboard(language, buttons)
    try:
        bot.edit_message_text(responses['lang_updated'][lang(cid)], cid, mid, reply_markup=keyboard, parse_mode="Markdown")
    except:
        pass
