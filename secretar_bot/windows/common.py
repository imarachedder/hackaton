from operator import itemgetter

from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select, Row, Checkbox, Radio
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format, Jinja, Multi, Text

from secretar_bot.handlers.common import common_handler
from secretar_bot.states import DefaultStates

main_window = Window(
        Format("Здравствуйте!\n"
               "Вас приветствует чат-бот 🤖 Cекретарь.\n"
               "Для обработки 🗣 аудиосовещания нажмите кнопку "
               "\n'Загрузить' ниже\n"
               "И следуйте дальнейшим шагам"),
        Button(
            text=Format("Загрузить аудио запись"),
            id="btn_load",
            on_click=common_handler.go_next,
        ),
        state=DefaultStates.main,
        getter=common_handler.get_message_types
    )

voice_select_window = Window(
        Jinja("Выберите формат выходного файла-протокола\n"
               "Также можете выбрать дополнительные параметры файла\n"
               "И прикрепите аудиофайл\n\n"
               "Поддерживаются следующие типы:\n"
               "〰 .ogg;\n"
               "〰 .mp3;\n"
               "〰 .wav.\n"),
        Button(text=Format("Назад"), on_click=common_handler.back, id='btn_back'),
        Row(
            Radio(
                Format("🔘 {item[name]}"),
                Format("⚪️{item[name]}"),
                items="message_types",
                item_id_getter=itemgetter('id'),
                id="output_file_select",
                on_click=common_handler.select
            ),
        ),
        Checkbox(
            Const("✓ Шифровать файл"),
            Const("Шифровать файл"),
            id="check",
            default=False,
            on_click=common_handler.set_password,
        ),
        MessageInput(content_types=[ContentType.DOCUMENT, ContentType.VOICE], func=common_handler.on_voice_sent),
        getter=common_handler.get_message_types,
        state=DefaultStates.get_voice_message,
    )

error_window = Window(
        Jinja("Ой... Произошла ошибка 😿\n\n"
               "Попробуйте еще раз"),
        Button(text=Format("Вернуться к выбору"), on_click=common_handler.back, id='btn_back'),
        state=DefaultStates.error,
    )

# like_window = Window(
#         Const("💋Спасибо за вашу оценку!💋\n"
#               "Мы знали, что вам этот курс понравится!😍\n"),
#         Button(text=Format("Вернуться назад"), on_click=common_handler.back, id='btn_back'),
#         state=DefaultStates.like,
#     )
#
# dislike_window = Window(
#         Const("😭Жаль, что вам не подошел данный курс💀\n\n"
#               "Наш чат-бот🤕 будет усерднее искать в следующий раз!\n"
#               "Поробуйте указать доп. параметры вакансии💼 мечты\n\n"
#               "Бот попробует еще раз дать вам то, что вы заслуживаете!🤩"),
#         Button(text=Format("Вернуться назад"), on_click=common_handler.back, id='btn_back'),
#         state=DefaultStates.dislike,
#     )

result_window = Window(
        Const("После обработки аудиофайла был получен следующий протокол:\n"),
        # Row(
        #     Button(text=Format("👍🏻"), on_click=common_handler.like, id='btn_like'),
        #     Button(text=Format("👎"), on_click=common_handler.dislike, id='btn_dislike'),
        # ),
        StaticMedia(
            path="C:\\Users\\denchik\\PycharmProjects\\parser_hackai\\README.md",
            type=ContentType.DOCUMENT,
        ),
        Button(text=Format("Вернуться в меню"), on_click=common_handler.back, id='btn_back'),
        state=DefaultStates.result
    )