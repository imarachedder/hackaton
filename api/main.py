from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
import api.router as main_router
import requests
app = FastAPI()

main_router.init(app)


def perform_transcription(audio_file: UploadFile) -> str:
    transcript = ""
    # Add your transcription logic here
    return transcript

def get_list_of_output_files() -> List[str]:
    output_files = ['file1.txt', 'file2.txt', 'file3.txt']
    return output_files

@app.post("/transcribe")
async def transcribe(audio_file: UploadFile = File(...)):
    transcript = perform_transcription(audio_file)
    return JSONResponse(content={'transcript': transcript})

@app.get("/output_files")
async def get_output_files():
    output_files = get_list_of_output_files()
    return JSONResponse(content={'output_files': output_files})

