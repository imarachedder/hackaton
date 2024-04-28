import os.path
from pathlib import Path
from typing import Any

import requests
from aiogram.types import Message, File
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.input import MessageInput

from gb_bot.states import DefaultStates
from gb_bot.main import _gb_bot


class CommonHandler:
    url = 'https://endless-presently-basilisk.ngrok-free.app'
    async def _download_file(self, path, file_id: str):
        file = await _gb_bot.bot.get_file(file_id=file_id)
        file_path = file.file_path
        Path(f"{path}/{'/'.join(file_path.split('/')[:-1])}").mkdir(parents=True, exist_ok=True)
        destination = f"{path}/{file_path}"
        await _gb_bot.bot.download_file(file_path=file_path, destination=destination)
        return destination

    async def select(self, callback: ChatEvent, select: Any,
                     dialog_manger: DialogManager,
                     item_id: str):
        if int(item_id) == 1:
            await dialog_manger.switch_to(DefaultStates.get_voice_message)
        elif int(item_id) == 2:
            await dialog_manger.switch_to(DefaultStates.get_file_message)
        elif int(item_id) == 3:
            await dialog_manger.switch_to(DefaultStates.get_url_message)
        else:
            await dialog_manger.switch_to(DefaultStates.get_text_message)

    async def back(self, callback: ChatEvent, select: Any, dialog_manager: DialogManager,):
        await dialog_manager.switch_to(DefaultStates.main)

    async def on_voice_sent(self, message: Message,
                            widget: MessageInput,
                            dialog_manager: DialogManager,):
        voice_id = message.voice.file_id
        path = "../files"
        file_path = await self._download_file(file_id=voice_id, path=path)
        upload_file = {'file': (file_path, open(file_path, 'rb'), f'application/{file_path.split(".")[-1]}')}
        request = requests.post(url=f'{self.url}/recommend_audio/',
                                headers={'accept': 'application/json'},
                                files=upload_file)
        result = request.json()
        print(result)
        has_error = result.get('detail', False)
        if has_error:
            await dialog_manager.switch_to(DefaultStates.error)
            return
        dialog_manager.dialog_data['result'] = result
        await dialog_manager.switch_to(DefaultStates.result)

    async def on_file_sent(self, message: Message,
                            widget: MessageInput,
                            dialog_manager: DialogManager,):
        document_id = message.document.file_id
        path = "../files"
        file_path = await self._download_file(file_id=document_id, path=path)
        upload_file = {'file': (file_path, open(file_path, 'rb'), f'application/{file_path.split(".")[-1]}')}
        request = requests.post(url=f'{self.url}/recommend/',
                                headers={'accept': 'application/json'},
                                files=upload_file)
        result = request.json()
        has_error = result.get('detail', False)
        if has_error:
            await dialog_manager.switch_to(DefaultStates.error)
            return
        dialog_manager.dialog_data['result'] = result
        await dialog_manager.switch_to(DefaultStates.result)

    async def on_text_sent(self, message: Message,
                           widget: MessageInput,
                           dialog_manager: DialogManager, ):
        text = message.text
        request = requests.post(url=f'{self.url}/recommend_text/',
                                headers={'accept': 'application/json',
                                         'Content-Type': 'application/json'},
                                json={'text': text})
        result = request.json()
        has_error = result.get('detail', False)
        if has_error:
            await dialog_manager.switch_to(DefaultStates.error)
            return
        dialog_manager.dialog_data['result'] = result
        await dialog_manager.switch_to(DefaultStates.result)

    async def on_url_sent(self, message: Message,
                           widget: MessageInput,
                           dialog_manager: DialogManager, ):
        text = message.text
        request = requests.post(url=f'{self.url}/recommend_link/',
                                headers={'accept': 'application/json',
                                         'Content-Type': 'application/json'},
                                json={'url': text})
        result = request.json()
        has_error = result.get('detail', False)
        if has_error:
            await dialog_manager.switch_to(DefaultStates.error)
            return
        dialog_manager.dialog_data['result'] = result
        await dialog_manager.switch_to(DefaultStates.result)

    async def get_message_types(self, *args, **kwargs):
        message_types = [{'id': 1, 'name': 'Голосовое сообщение'},
                         {'id': 2, 'name': 'Файл с резюме'},
                         {'id': 3, 'name': 'Ссылка на резюме'},
                         {'id': 4, 'name': 'Текстовое сообщение'}]
        return {'message_types': message_types}

    async def get_courses(self, dialog_manager: DialogManager, *args, **kwargs):
        text = dialog_manager.dialog_data['result']
        return text

    async def dislike(self, callback: ChatEvent, button: Any, dialog_manager: DialogManager):
        await dialog_manager.switch_to(DefaultStates.dislike)

    async def like(self, callback: ChatEvent, button: Any, dialog_manager: DialogManager):
        await dialog_manager.switch_to(DefaultStates.like)

common_handler = CommonHandler()