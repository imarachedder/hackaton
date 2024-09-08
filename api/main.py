from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
import pathlib
import os
import io
import shutil
from transcription import transcription

app = FastAPI()


def perform_transcription(audio_file: UploadFile) -> str:
    # Save the uploaded file temporarily
    temp_audio_path = pathlib.Path("files")/"voice"/audio_file.filename
    temp_audio_path.parent.mkdir(parents=True, exist_ok=True)

    with open(temp_audio_path, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    # Perform transcription
    transcript = transcription(temp_audio_path)

    # Clean up the temporary files
    temp_audio_path.unlink()

    return transcript


def get_list_of_output_files() -> List[str]:
    output_files = ['file1.txt', 'file2.txt', 'file3.txt']
    return output_files


@app.post("/get_protocol/")
async def transcribe(audio_file: UploadFile = File(...)):
    transcript = perform_transcription(audio_file)
    return JSONResponse(content={'transcript': transcript})


@app.get("/output_files")
async def get_output_files():
    output_files = get_list_of_output_files()
    return JSONResponse(content={'output_files': output_files})
