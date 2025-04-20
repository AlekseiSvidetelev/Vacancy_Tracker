import time
from abc import ABC, abstractmethod
from typing import Any

import requests


class VacancyAPI(ABC):
    """Абстрактный базовый класс для запроса вакансий"""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict[str, Any]]:
        pass


class HeadHunterAPI(VacancyAPI):
    """Класс для получения вакансий с HeadHunter"""

    vacancies: list[dict[str, Any]]
    base_url: str
    headers: dict[str, str]
    params: dict[str, Any]
    request_time: float

    def __init__(self) -> None:
        self.vacancies = []
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__request_time: float = 0.0

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}. "
            f"Получено вакансий: {len(self.vacancies)}, "
            f"Время запроса: {self.__request_time}"
        )

    def __str__(self) -> str:
        return f"{self.vacancies}"

    def __connect(self, __params: dict[Any, Any]) -> requests.Response:
        """Метод для подключения к API"""
        try:
            response = requests.get(self.__base_url, headers=self.__headers, params=self.__params)
            if response.status_code != 200:
                print("Нет соединения с сервисом API для получения данных")
                raise ConnectionError("Нет соединения с сервисом API для получения данных")
            return response
        except Exception as e:
            print(f"Ошибка подключения к API: {e}")

    def get_vacancies(self, keyword: str) -> list[dict[str, Any]]:
        """Основной метод для получения вакансий из items"""
        self.__params["text"] = keyword
        try:
            time_start = time.time()
            while self.__params["page"] != 20:
                response = self.__connect(self.__params)
                items = response.json().get("items", [])
                if not items:
                    break
                self.vacancies.extend(items)
                self.__params["page"] += 1
                time.sleep(0.25)
            self.__request_time = round((time.time() - time_start), 1)
            return self.vacancies
        except Exception as e:
            print(f"Ошибка при получении вакансий: {e}")


if __name__ == "__main__":
    hh = HeadHunterAPI()
    res = hh.get_vacancies("тестировщик")
    print(res)
    print(hh)
    print(repr(hh))
