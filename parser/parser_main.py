import json
import pprint
import re

from bs4 import BeautifulSoup as bs
import requests as requests


class CoursesParser:
    courses = []

    def __init__(self, url: str = 'https://gb.ru/courses/all'):
        r = requests.get(url)
        self.soup = bs(r.text, 'html.parser')

    def get_main_courses_info(self):
        url_data = self.soup.find_all('a', {'class': 'card_full_link'})
        name_data = self.soup.find_all('span', {'class': 'direction-card__title-text'})
        description_data = self.soup.find_all('div', {'class': 'direction-card__text'})
        for idx, url in enumerate(url_data):
            clear_name = name_data[idx].get_text(strip=True).replace('\xa0', ' ')
            clear_description = description_data[idx].get_text(strip=True).replace('\xa0', ' ')
            main_info_url = str(url['href'])
            main_info_request = requests.get(main_info_url)
            full_info = bs(main_info_request.text, 'html.parser')
            tags_data = full_info.find('div', {'class': 'gkb-promo__tag-wrapper promo-tech__wrapper'})
            additional_data = full_info.find('p', {'class': 'gkb-promo__text'})
            recommend_container = full_info.find('div', {'class': 'gkb-recon gkb-layout-wrapper'})
            recommendations = []
            if recommend_container is not None:
                recommend_data = recommend_container.find_all('div', {'class': 'gkb-recon__card'})
                if recommend_data is not None:
                    for recommendation in recommend_data:
                        title = recommendation.find('p').get_text(strip=True)
                        subtitle = recommendation.find('span').get_text().replace('\n', ' ').replace('\xa0', ' ')
                        text = f'{title} {subtitle}'
                        recommendations.append(text)
            if additional_data is None:
                additional_data = full_info.find('p', {'class': 'promo__description'})
            tags = []
            if tags_data is not None:
                for course_info in tags_data.find_all('span'):
                    tags.append(course_info.get_text(strip=True))

            main_info = {
                'url': main_info_url,
                'name': clear_name,
                'description': clear_description,
                'additional_info': '',
                'tags': tags[:-1],
                'recommendations': recommendations,
                }
            if additional_data is not None:
                main_info['additional_info'] = additional_data.get_text(strip=True)
            self.courses.append(main_info)

    def save_to_json(self):
        json_string = json.dumps(self.courses, ensure_ascii=False)
        with open('output_courses.json', 'w', encoding='utf8') as output_file:
            output_file.write(json_string)

    def __str__(self):
        return self.courses


parser = CoursesParser(url='https://gb.ru/courses/all')
parser.get_main_courses_info()
parser.save_to_json()