import json
import pprint
import re

from bs4 import BeautifulSoup as bs
import requests as requests


class CoursesParser:
    courses = []



def get_main_courses_info(self):
    import re
    url_data = self.soup.select('script')
    for item in url_data:
        data = re.search('JSON\.parse\(\((.*)\)\)', str(item))
        size_data = re.search('size.push\((.*)\)', str(item))
        if data is not None:
            json_data = data.group(1).replace('&quot;', '"').replace('&#', '')
            print(json_data)
        if size_data is not None:
            pprint.pp(json.loads(size_data.group(1)))