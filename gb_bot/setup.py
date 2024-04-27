from aiogram_dialog import Dialog

from gb_bot.windows.common import *


def setup_default_dialogs():
    dialog = Dialog(
        main_window,
        voice_select_window,
        file_select_window,
        text_select_window,
        url_select_window,
        result_window,
        like_window,
        dislike_window,
    )
    return dialog
