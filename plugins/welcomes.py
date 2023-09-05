from config import *

from functions.validate_group import bot_welcome_into_group

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def command_hi(message):
    cid = message.chat.id
    mid = message.message_id
    id_user = message.from_user.id
    group_lang = lang(cid)
    user_name = message.from_user.first_name
    is_private = False
    if message.chat.type == "private":
        is_private = True


    response_message = bot_welcome_into_group(is_private, cid, group_lang, id_user, user_name)[1]
    bot.send_message(cid, response_message)
    response_message = f"group lang {group_lang}"
    bot.send_message(cid, response_message)
    '''
    if message.chat.type != "private":
        response_message = responses['group_generic_welcome'][group_lang]
        bot.send_message(cid, response_message)
    '''
