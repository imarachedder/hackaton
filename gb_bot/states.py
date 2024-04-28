from aiogram.fsm.state import StatesGroup, State


class DefaultStates(StatesGroup):
    main = State()
    get_voice_message = State()
    get_text_message = State()
    get_url_message = State()
    get_file_message = State()
    result = State()
    like = State()
    dislike = State()
    error = State()