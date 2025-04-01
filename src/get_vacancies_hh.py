import os
from typing import Any
import requests
import time
from abc import ABC, abstractmethod
from src.utils import save_json_file

from dotenv import load_dotenv

load_dotenv()
AGENT_HH_API = os.environ.get("AGENT_HH_API")
TOKEN_HH_API = os.environ.get("TOKEN_HH_API")


class VacancyAPI(ABC):
    """Абстрактный базовый класс для API"""

    @abstractmethod
    def __init__(self, file_worker: str):
        self.file_worker = file_worker



class HeadHunterAPI(VacancyAPI):
    """Класс для работы с API HeadHunter"""


    def __init__(self, file_worker=None, search_word=None, number_vacancies=None):
        super().__init__(file_worker)
        self.__vacancies = []
        self.__file_worker = file_worker if file_worker else "vacancies.json"
        self.search_word = search_word
        self.number_vacancies = number_vacancies if number_vacancies else 100
        self.__connected_status = False
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {AGENT_HH_API: TOKEN_HH_API}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"Название файла = '{self.file_worker}', "
                f"Слово для поиска = '{self.search_word}', "
                f"Найдено вакансий = {len(self.vacancies)}, "
                f"Статус подключения = {self.connected_status}")

    def __str__(self):
        return f"Найдено вакансий: {len(self.vacancies)}"

    @property
    def vacancies(self):
        """ Геттер для доступа к списку вакансий """
        return self.__vacancies

    @property
    def connected_status(self):
        """ Геттер для статуса подключения """
        return self.__connected_status

    @property
    def url(self):
        return self.__url

    @property
    def headers(self):
        return self.__headers

    def check_connected_status(self) -> None:
        """Метод для проверки подключения"""
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                self.__connected_status = True
        except Exception as e:
            self.__connected_status = False
            print(f"Ошибка подключения: {e}")




    def get_vacancies_hh(self, keyword: str, number_vacancies: int = 100) -> None:
        """Загружает вакансии с проверкой подключения перед каждым запросом"""
        self.__params["text"] = keyword
        self.__params["page"] = 0
        self.__vacancies = []

        while True:
            self.check_connected_status()
            if self.__connected_status is False:
                print("Нет подключения к API. Загрузка прервана.")
                break
            try:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                data = response.json()
                self.__vacancies.extend(data["items"])
                if len(self.__vacancies) >= number_vacancies:
                    self.__vacancies = self.__vacancies[:number_vacancies]
                    break
                if self.__params["page"] >= data.get("pages", 0) - 1:
                    break

                self.__params["page"] += 1
                time.sleep(0.5)

            except Exception as e:
                print(f"Ошибка при загрузке данных: {e}")
                break

    def save_to_json(self, filename: str) -> None:
        """Сохранение полученных вакансий в JSON-файл"""
        try:
            result = {
                "items": self.vacancies,
                "found": len(self.vacancies),
                "pages": self.__params['page'] + 1,
                "page": self.__params['page'],
                "per_page": self.__params['per_page'],
                "alternate_url": f"https://hh.ru/search/vacancy?text={self.__params['text']}"
            }
            save_json_file(filename, result)
            print(f"Данные успешно записаны в файл: {filename}")
        except Exception as e:
            print(f"Ошибка '{Exception}' при сохранении файла: {e}")



if __name__ == "__main__":
    hh_api = HeadHunterAPI("vacancies.json", "Python developer", 250)
    hh_api.load_vacancies("Python developer", 250)
    print(repr(hh_api))
    hh_api.save_to_json("vacancies.json")
    print(str(hh_api))
