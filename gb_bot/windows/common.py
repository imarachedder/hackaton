from operator import itemgetter

from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select, Row, NumberedPager, ScrollingGroup, PrevPage, NextPage, SwitchTo, \
    Url
from aiogram_dialog.widgets.kbd.pager import DEFAULT_PAGE_TEXT, DEFAULT_PREV_BUTTON_TEXT, DEFAULT_CURRENT_PAGE_TEXT, \
    CurrentPage
from aiogram_dialog.widgets.text import Const, Format, Jinja, Multi, Text

from gb_bot.handlers.common import common_handler
from gb_bot.states import DefaultStates

main_window = Window(
        Format("Здравствуйте!\n"
               "Вас приветствует чат-бот🤖 GeekBrains."
               "Мы поможем Вам выбрать программу обучения на основе предоставленной вами "
               "информации!\n"
               "Выберите один из трех вариантов загрузки резюме вашей мечты!"),
        ScrollingGroup(
            Select(
                Format("{item[name]}"),
                items="message_types",
                item_id_getter=itemgetter('id'),
                id="message_select",
                on_click=common_handler.select,
            ),
            width=1,
            height=4,
            hide_pager=True,
            id="scroll_no_pager1",
        ),
        state=DefaultStates.main,
        getter=common_handler.get_message_types
    )

voice_select_window = Window(
        Format("Запишите голосовое сообщение с описанием вакансии\n"
               "Расскажите самые важные моменты, которые вам интересны в вакансии"),
        Button(text=Format("Назад"), on_click=common_handler.back, id='btn_back'),
        MessageInput(content_types=[ContentType.VOICE], func=common_handler.on_voice_sent),
        state=DefaultStates.get_voice_message,
    )

file_select_window = Window(
        Format("Прикрепите файл с описанием вакансии💼\n"
              "Используйте форматы .docx, .pdf, пожалуйста😇"),
        Button(text=Format("Назад"), on_click=common_handler.back, id='btn_back'),
        MessageInput(content_types=[ContentType.DOCUMENT], func=common_handler.on_file_sent),
        state=DefaultStates.get_file_message,
    )

text_select_window = Window(
        Const("Напишите описание вакансии💼, которая вам очень понравилась!\n"
              "Можете укзать только основные моменты, которые вас привлекают!"),
        Button(text=Format("Назад"), on_click=common_handler.back, id='btn_back'),
        MessageInput(content_types=[ContentType.TEXT], func=common_handler.on_text_sent),
        state=DefaultStates.get_text_message,
    )

url_select_window = Window(
        Const("Отправьте ссылку на вакансию💼, которая вам очень понравилась!\n"
              "Остальное не важно - мы сделаем все сами!🧐"),
        Button(text=Format("Назад"), on_click=common_handler.back, id='btn_back'),
        MessageInput(content_types=[ContentType.TEXT], func=common_handler.on_url_sent),
        state=DefaultStates.get_url_message,
    )

like_window = Window(
        Const("💋Спасибо за вашу оценку!💋\n"
              "Мы знали, что вам этот курс понравится!😍\n"),
        Button(text=Format("Вернуться назад"), on_click=common_handler.back, id='btn_back'),
        state=DefaultStates.like,
    )

dislike_window = Window(
        Const("😭Жаль, что вам не подошел данный курс💀\n"
              "Наш чат-бот🤕 будет усерднее думать в следующий раз!\n"
              "Поробуйте указать доп. параметры вашей вакансии💼 мечты"
              "Бот попробует еще раз дать вам то, что вы заслуживаете!🤩"),
        Button(text=Format("Вернуться назад"), on_click=common_handler.back, id='btn_back'),
        state=DefaultStates.dislike,
    )

result_window = Window(
        Const("🥳Поздравляем!🥳\n"
              "Мы нашли то, что вам понравится!😍\n"
              "И это...🫣\n"),
        Jinja('😱{{ course }} \n'
              'Какие навыки получите: 🤩{{ tech_skills }}\n'
              'Если это именно то, 🥰 что вам нужно, то поставьте 👍🏻, \n'
              'а если нет, то 👎'),
        Row(
            Button(text=Format("👍🏻"), on_click=common_handler.like, id='btn_like'),
            Button(text=Format("👎"), on_click=common_handler.dislike, id='btn_dislike'),
        ),
        Button(text=Format("Вернуться в меню"), on_click=common_handler.back, id='btn_back'),
        state=DefaultStates.result,
        getter=common_handler.get_courses
    )