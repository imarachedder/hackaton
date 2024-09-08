import asyncio
import json

from fastapi import Response, Body, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse
from api.main import app


@app.get("/api/v1/upload_file/")
async def upload_file(data=UploadFile):
    output_info = []
    #Сюда вписать логику с работой файла с моделью
    result_file = 'Протокол.docx'
    return FileResponse(path='Протокол.xlsx', filename='Статистика покупок.xlsx', media_type='multipart/form-data')

