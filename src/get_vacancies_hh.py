from typing import Any
import requests
import time
from abc import ABC, abstractmethod
from utils import load_json_file


class Vacancy(ABC):
    """Абстрактный базовый класс для API"""

    vacancies: list[dict[str, Any]]

    @abstractmethod
    def __init__(self):
        self.vacancies = []
        self.__connect = False

    @property
    def connect(self):
        return self.__connect

    def __repr__(self):
        return f"{type(self.connect)}"



class HeadHunterAPI(Vacancy):
    """ Класс для работы с API HeadHunter """

    url: str
    headers: dict[str, str]
    params: dict[str, str|int]

    def __init__(self):
        super().__init__()
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    @property
    def url(self):
        return self.__url

    @property
    def headers(self):
        return self.__headers

    def load_vacancies(self, keyword: str, max_pages: int = 20) -> None:
        """ Получение вакансий по ключевому слову """
        self.params['text'] = keyword
        self.params['page'] = 0

        while self.params.get('page') < max_pages:
            try:
                response = requests.get(self.url, headers=self.headers, params=self.params)
                if response.status_code != 200:
                    raise Exception(f"Ошибка: {response.status_code}")
                data = response.json()
                self.vacancies.extend(data['items'])
                if self.params.get('page') >= data.get('pages') - 1:
                    break
                self.params['page'] += 1
                time.sleep(0.5)
            except Exception as e:
                print(f"Ошибка '{Exception}': {e}")
                break

    def save_to_json(self, filename: str) -> None:
        """Сохранение полученных вакансий в JSON-файл"""
        try:
            result = {
                "items": self.vacancies,
                "found": len(self.vacancies),
                "pages": self.params['page'] + 1,
                "page": self.params['page'],
                "per_page": self.params['per_page'],
                "alternate_url": f"https://hh.ru/search/vacancy?text={self.params['text']}"
            }
            load_json_file(filename, result)
            print(f"Данные успешно записаны в файл: {filename}")
        except Exception as e:
            print(f"Ошибка '{Exception}' при сохранении файла: {e}")


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    hh_api.load_vacancies("Python developer", max_pages=1)
    hh_api.save_to_json("vacancies.json")
    print(repr(HeadHunterAPI.connect))
    print(f"Найдено вакансий: {len(hh_api.vacancies)}")

