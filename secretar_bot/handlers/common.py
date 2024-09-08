import os.path
import time
from pathlib import Path
from typing import Any, Union

import requests
from aiogram.types import Message
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.input import MessageInput

from secretar_bot.states import DefaultStates
from secretar_bot.main import _secretar_bot


class CommonHandler:
    async def _download_file(self, path, file_id: str):
        file = await _secretar_bot.bot.get_file(file_id=file_id)
        file_path = file.file_path
        Path(f"{path}/{'/'.join(file_path.split('/')[:-1])}").mkdir(parents=True, exist_ok=True)
        destination = f"{path}/{file_path}"
        await _secretar_bot.bot.download_file(file_path=file_path, destination=destination)
        return destination

    async def next_file(self, callback: ChatEvent, widget: Any, dialog_manager: DialogManager,):
        return await dialog_manager.next()

    async def select(self, callback: ChatEvent, widget: Any,
                     dialog_manager: DialogManager,
                     item_id: str):
        dialog_manager.dialog_data['file'] = item_id

    async def back(self, callback: ChatEvent, widget: Any, dialog_manager: DialogManager,):
        await dialog_manager.switch_to(DefaultStates.main)

    async def go_next(self, callback: ChatEvent, widget: Any, dialog_manager: DialogManager,):
        await dialog_manager.switch_to(DefaultStates.get_voice_message)

    async def set_password(self, callback: ChatEvent, widget: Any,
                           dialog_manager: DialogManager):
        dialog_manager.dialog_data['set_password'] = not widget.is_checked()

    async def on_voice_sent(self, message: Message,
                            widget: MessageInput,
                            dialog_manager: DialogManager,):
        voice = message.voice
        document = message.document
        get_transcription = dialog_manager.dialog_data.get('is_transcription', False)
        set_password = dialog_manager.dialog_data.get('set_password', False)

        if document is None:
            voice_id = voice.file_id
        else:
            voice_id = document.file_id

        #Указываем путь к аудиофайлу
        path = "../files"
        #Скачиваем файл с ТГ
        file_path = await self._download_file(file_id=voice_id, path=path)
        print(file_path)
        #Передаем скачанный файл на API с моделькой
        upload_file = {'file': (file_path, open(file_path, 'rb'), f'application/{file_path.split(".")[-1]}')}
        #Отправляем запрос на получение Протокола
        request = requests.post(url=f'{"localhost"}/get_protocol/',
                                headers={'accept': 'application/json'},
                                files=upload_file)
        result = request.json()
        #Проверяем, есть ли ошибки в ответе
        has_error = result.get('errors', False)

        if has_error:
            await dialog_manager.switch_to(DefaultStates.error)
            return
        if int(dialog_manager.dialog_data['file']) == 1:
            await dialog_manager.switch_to(DefaultStates.docx_result)
        else:
            await dialog_manager.switch_to(DefaultStates.pdf_result)
        return

    async def get_message_types(self, *args, **kwargs):
        message_types = [{'id': 1, 'name': '.docx'},
                         {'id': 2, 'name': '.pdf'}]
        return {'message_types': message_types}

    async def get_transcription(self, callback: ChatEvent, widget: Any,
                           dialog_manager: DialogManager):
        dialog_manager.dialog_data['is_transcription'] = not widget.is_checked()

    async def get_protocols(self, callback: ChatEvent, widget: Any,
                           dialog_manager: DialogManager):
        return dialog_manager.dialog_data['protocol']

common_handler = CommonHandler()
