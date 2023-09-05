from config import *

def bot_welcome_into_group(is_private, id_group, group_lang, id_user, user_name):

    # data = get_group_data(id_group)
    data = {
        "132223231213312": {},
        "validated": False
    }
    g_admins = [247295279, 239822769]
    validated = False

    # response_message = responses['group_generic_welcome'][group_lang].format(user_name)
    
    if is_private is False:

        if data["validated"]:
            validated = True
            response_message = "Gracias por meterme al grupo de nuevo."
        else:
            if id_user in g_admins:
                validated = True
            if id_group not in data and is_private is False:
                validated = False
                response_message = "Este no es mi grupo "

        response_message = responses['group_generic_welcome'][group_lang].format(user_name)
    
    return validated, response_message
