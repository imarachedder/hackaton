Such simple tg bot and parser
1. Prepare venv
   create venv:
   
   ```python3 -m venv venv```
   
2. init venv
   
   linux: ```source .\venv\bin\activate```
   windows: ```.\venv\Scripts\activate```
   
3. install requirements
   
   ```pip install -r requirements.txt```
4. launch parser (It may take a some time to parse all necessary course data)
   
   ```python parser/parser_main.py```
   
   After complete you can see a JSON file called `output_courses.json`
   
5. launch tg bot
    
   ```python gb_bot run.py```
   
6. go to https://t.me/gb_course_search_bot and it try to give a personality course for you

7. (Дополнительно установить ffmpeg (менеджер pip не всегда срабатывает)
    при установке в конду использовать conda install -c conda-forge ffmpeg
    или скачать отдельно с сайта https://ffmpeg.org/download.html пакеты кодека ffmpeg
    Установите переменные среды с помощью путей к двоичным файлам FFmpeg:
    В Windows запустите:
    SET PATH=D:\path\to\transcription\bin;%PATH%
    В Unix или MacOS запустите:
    export FFMPEG_PATH=/path/to/ffmpeg: