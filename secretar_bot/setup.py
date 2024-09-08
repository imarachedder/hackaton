from aiogram_dialog import Dialog

from secretar_bot.windows.common import *


def setup_default_dialogs():
    dialog = Dialog(
        main_window,
        voice_select_window,
        result_window,
        # like_window,
        # dislike_window,
        error_window
    )
    return dialog
