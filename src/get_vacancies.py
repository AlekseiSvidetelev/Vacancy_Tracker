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

    file_worker: str

    @abstractmethod
    def __init__(self, file_worker: str):
        self.file_worker = file_worker


class HeadHunterAPI(VacancyAPI):
    """Класс для работы с API HeadHunter"""

    vacancies: list
    file_worker: str
    search_word: str
    number_vacancies: int
    connected_status: bool
    url: str
    headers: dict[str, str]
    params: dict[str, str | int]

    def __init__(self, file_worker: str, number_vacancies: int, search_word: str = ""):
        super().__init__(file_worker)
        self.__vacancies: list[dict[str, Any]] = []
        self.__file_worker = file_worker if file_worker else "vacancies.json"
        self.search_word = search_word
        self.number_vacancies = number_vacancies if number_vacancies else 100
        self.__connected_status = False
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers: dict[str, str] = {AGENT_HH_API: TOKEN_HH_API}
        self.__params: Any = {"text": "", "page": 0, "per_page": 100}

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"Название файла = '{self.file_worker}', "
            f"Слово для поиска = '{self.search_word}', "
            f"Найдено вакансий = {len(self.vacancies)}, "
            f"Статус подключения = {self.connected_status}"
        )

    def __str__(self) -> str:
        return f"Найдено вакансий: {len(self.vacancies)}"

    @property
    def vacancies(self) -> list[dict[str, Any]]:
        """Геттер для доступа к списку вакансий"""
        return self.__vacancies

    @property
    def connected_status(self) -> bool:
        """Геттер для статуса подключения"""
        return self.__connected_status

    @property
    def url(self) -> str:
        return self.__url

    @property
    def headers(self) -> dict[str, str]:
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

    def get_vacancies_hh(self, keyword: str) -> None:
        """Загружает вакансии с проверкой подключения перед каждым запросом"""
        try:
            self.check_connected_status()
            self.search_word = keyword
            self.__params["text"] = self.search_word
            self.__params["page"] = 0
            self.__vacancies = []
            while True:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                if self.__connected_status is False:
                    print("Нет подключения к API. Загрузка прервана.")
                    raise ConnectionError("Нет подключения к API. Загрузка прервана.")
                data = response.json()
                self.__vacancies.extend(data["items"])
                if len(self.__vacancies) >= self.number_vacancies:
                    self.__vacancies = self.__vacancies[: self.number_vacancies]
                    break
                if self.__params["page"] >= data.get("pages", 0) - 1:
                    break
                self.__params["page"] += 1
                time.sleep(0.5)
        except Exception as e:
            print(f"Ошибка при получении данных {Exception}: {e}")

    def save_to_json(self) -> None:
        """Сохранение полученных вакансий в JSON-файл"""
        filename = self.file_worker
        try:
            if len(self.vacancies) == 0:
                print("Список вакансий для записи пустой")
                raise ValueError("Нет данных для записи")
            result = {
                "items": self.vacancies,
                "found": len(self.vacancies),
                "pages": self.__params["page"] + 1,
                "page": self.__params["page"],
                "per_page": self.__params["per_page"],
                "alternate_url": f"https://hh.ru/search/vacancy?text={self.__params['text']}",
            }
            save_json_file(filename, result)
            print(f"Данные успешно записаны в файл: {filename}")
        except Exception as e:
            print(f"Ошибка '{Exception}' при сохранении файла: {e}")


if __name__ == "__main__":
    hh_api = HeadHunterAPI("vacancies.json", 109)
    hh_api.get_vacancies_hh("Python")
    print(repr(hh_api))
    hh_api.save_to_json()
    print(str(hh_api))
