# from docx import Document
#
# def fill_unofficial_protocol(template_path, output_path, data):
#     # Открытие шаблона документа
#     doc = Document(template_path)
#
#     # Замена данных
#     for paragraph in doc.paragraphs:
#         if 'ТЕМА ВСТРЕЧИ' in paragraph.text:
#             paragraph.text = f"ТЕМА ВСТРЕЧИ: {data['тема']}"
#         elif 'ДАТА:' in paragraph.text:
#             paragraph.text = f"ДАТА: {data['дата']}"
#         elif 'ВРЕМЯ:' in paragraph.text:
#             paragraph.text = f"ВРЕМЯ: {data['время']}"
#         elif 'ДЛИТЕЛЬНОСТЬ:' in paragraph.text:
#             paragraph.text = f"ДЛИТЕЛЬНОСТЬ: {data['длительность']}"
#         elif 'УЧАСТНИКИ:' in paragraph.text:
#             paragraph.text = f"УЧАСТНИКИ: {', '.join(data['участники'])}"
#         elif 'Цель встречи' in paragraph.text:
#             paragraph.text = f"Цель встречи: {data['цель_встречи']}"
#
#     # Заполнение повестки дня и резюме обсуждений
#     for i, question in enumerate(data['вопросы'], 1):
#         doc.add_heading(f"Название вопроса {i}", level=1)
#         doc.add_paragraph(f"Докладчики: {', '.join(question['докладчики'])}")
#         doc.add_paragraph(f"Решение: {question['решение']}")
#         doc.add_paragraph(f"Контекст обсуждения: {question['контекст']}")
#         doc.add_paragraph(f"Время: {question['время']}")
#
#     # Сохранение нового документа
#     doc.save(output_path)
#
#
# # Пример данных для заполнения
# data_unofficial = {
#     'тема': 'Обсуждение стратегии компании',
#     'дата': '22.07.2024',
#     'время': '14:33',
#     'длительность': '00:15',
#     'участники': ['Петр', 'Игорь', 'Марина', 'Семен'],
#     'цель_встречи': 'Декларация целей компании на ближайшие 5 лет',
#     'вопросы': [
#         {
#             'докладчики': ['Игорь'],
#             'решение': 'Утвердить стратегию.',
#             'контекст': 'Обсуждали планы на 5 лет.',
#             'время': '00:10'
#         },
#         {
#             'докладчики': ['Петр'],
#             'решение': 'Не пришли к согласию.',
#             'контекст': 'Потребуется дополнительная проработка.',
#             'время': '00:05'
#         }
#     ]
# }
#
# # Заполнение неофициального шаблона
# fill_unofficial_protocol('Протокол. Шаблон неофициальный.docx', 'unformal.docx', data_unofficial)
#
#
# def fill_official_protocol(template_path, output_path, data):
#     doc = Document(template_path)
#
#     # Заполнение основной информации
#     for paragraph in doc.paragraphs:
#         if '[такой-то]' in paragraph.text:
#             paragraph.text = paragraph.text.replace('[такой-то]', data['тема'])
#         elif '№_____________' in paragraph.text:
#             paragraph.text = paragraph.text.replace('№_____________', data['номер'])
#         elif 'ПЕРЕЧЕНЬ ПОРУЧЕНИЙ' in paragraph.text:
#             doc.add_heading('Поручения', level=1)
#
#     # Заполнение участников
#     table = doc.tables[0]
#     for i, participant in enumerate(data['участники']):
#         table.cell(i + 1, 1).text = participant['должность']
#         table.cell(i + 1, 3).text = participant['фио']
#
#     # Заполнение повестки и решений
#     for i, вопрос in enumerate(data['вопросы'], 1):
#         doc.add_heading(f"{i}. {вопрос['название']}", level=1)
#         for решение in вопрос['решения']:
#             doc.add_paragraph(f"Докладчики: {', '.join(решение['докладчики'])}")
#             doc.add_paragraph(f"Решение: {решение['решение']}")
#             doc.add_paragraph(f"Контекст обсуждения: {решение['контекст']}")
#             doc.add_paragraph(f"Время: {решение['время']}")
#
#     # Заполнение поручений
#     doc.add_heading('ПЕРЕЧЕНЬ ПОРУЧЕНИЙ', level=1)
#     for поручение in data['поручения']:
#         doc.add_paragraph(f"Организация-исполнитель: {поручение['организация']}")
#         doc.add_paragraph(f"Задача: {поручение['задача']}")
#         doc.add_paragraph(f"Срок: {поручение['срок']}")
#
#     doc.save(output_path)
#
#
# # Пример данных для заполнения официального шаблона
# data_official = {
#     'тема': 'Обсуждение новой маркетинговой стратегии',
#     'номер': '12345',
#     'участники': [
#         {'должность': 'Директор', 'фио': 'Иван Иванов'},
#         {'должность': 'Менеджер', 'фио': 'Петр Петров'},
#         {'должность': 'Аналитик', 'фио': 'Мария Смирнова'}
#     ],
#     'вопросы': [
#         {
#             'название': 'Вопрос 1',
#             'решения': [
#                 {
#                     'докладчики': ['Иван Иванов'],
#                     'решение': 'Принято решение внедрить стратегию.',
#                     'контекст': 'Обсуждение рисков внедрения.',
#                     'время': '10:15'
#                 },
#                 {
#                     'докладчики': ['Петр Петров'],
#                     'решение': 'Дополнительно изучить рынок.',
#                     'контекст': 'Планирование этапов.',
#                     'время': '10:45'
#                 }
#             ]
#         }
#     ],
#     'поручения': [
#         {
#             'организация': 'Отдел маркетинга',
#             'задача': 'Разработать план по внедрению.',
#             'срок': '01.09.2024'
#         }
#     ]
# }
#
# # Заполнение официального шаблона
# fill_official_protocol('Протокол. Шаблон официальный.docx', 'official.docx', data_official)
#
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def extract_tasks(text):
    # Пример простого выделения задач из текста (может быть доработан в зависимости от структуры данных)
    tasks = "Задачи, извлеченные из текста"
    return tasks


def create_pdf_documents(transcription, summary):
    files = ["raw.pdf", "unformal.pdf", "official.pdf"]

    for file in files:
        # Создание PDF-документа
        c = canvas.Canvas(file, pagesize=letter)
        width, height = letter
        y_position = height - 50  # Начальная позиция текста по оси Y

        # Заголовок документа
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, y_position, "Протокол совещания")
        y_position -= 30

        # Количество спикеров (если нужно добавить конкретные данные, можно передать параметр)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_position, "Количество спикеров:")
        y_position -= 20

        # Транскрипция
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_position, "Транскрипция:")
        y_position -= 20
        c.setFont("Helvetica", 10)
        text = transcription.split('\n')
        for line in text:
            c.drawString(100, y_position, line)
            y_position -= 15
            if y_position < 50:
                c.showPage()  # Переход на новую страницу
                y_position = height - 50

        # Обработанный текст
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_position, "Обработанный текст:")
        y_position -= 20
        c.setFont("Helvetica", 10)
        text = summary.split('\n')
        for line in text:
            c.drawString(100, y_position, line)
            y_position -= 15
            if y_position < 50:
                c.showPage()
                y_position = height - 50

        # Поставленные задачи
        tasks = extract_tasks(transcription)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_position, "Поставленные задачи:")
        y_position -= 20
        c.setFont("Helvetica", 10)
        c.drawString(100, y_position, tasks)

        # Сохранение PDF-файла
        c.save()


# Пример данных
transcription = "Это пример транскрипции встречи. Спикер 1: Привет. Спикер 2: Привет."
summary = "Это обработанный текст встречи. Обсудили следующие вопросы."

# Создание PDF-документов
create_pdf_documents(transcription, summary)
