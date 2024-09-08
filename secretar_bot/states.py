from aiogram.fsm.state import StatesGroup, State


class DefaultStates(StatesGroup):
    main = State()
    preparing = State()
    get_voice_message = State()
    result = State()
    error = State()