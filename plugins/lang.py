from config import *

from functions.utils import create_keyboard


@bot.message_handler(commands=['lang'], func=lambda m: is_user(m.chat.id))
def lang_handler(m):
  "Función para actualizar el idioma del bot"
  cid = m.chat.id
  buttons = responses[f"lang_{lang(cid)}_buttons"]
  keyboard = create_keyboard(buttons)
  bot.send_message(cid, responses['lang'][lang(cid)], reply_markup=keyboard, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data in ['en', 'es','eus'])
def callback_handler(call):
    "Función para manejar el uso de los botones para cambiar el idioma"
    cid = call.message.chat.id
    mid = call.message.message_id
    language = call.data
    update_lang(cid, language)
    buttons = responses[f"lang_{language}_buttons"]
    keyboard = create_keyboard(buttons)
    try:
        bot.edit_message_text(responses['lang_updated'][lang(cid)], cid, mid, reply_markup=keyboard, parse_mode="Markdown")
    except:
        pass
