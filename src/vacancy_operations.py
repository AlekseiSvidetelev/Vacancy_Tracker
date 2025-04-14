import re
from typing import Any


# from src.utils import clean_search_teg


class Vacancy:
    """Класс представления вакансии"""

    vacancy_id: int
    name: str
    area: str
    salary_from: int
    url: str
    snippet_requirement: str
    snippet_responsibility: str

    __slots__ = ("vacancy_id", "name", "area", "salary_from", "url", "snippet_requirement", "snippet_responsibility")

    def __init__(
        self,
        vacancy_id: int,
        name: str,
        area: str,
        salary_from: int,
        url: str,
        snippet_requirement: str,
        snippet_responsibility: str,
    ):
        self.vacancy_id = vacancy_id
        self.name = name
        self.area = area
        self.salary_from = salary_from
        self.url = url
        self.snippet_requirement = snippet_requirement
        self.snippet_responsibility = snippet_responsibility

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary_from < other.salary_from

    def __str__(self) -> str:
        return (
            f"ID: {self.vacancy_id}\n"
            f"Название вакансии: {self.name}\n"
            f"Зарплата от: {'не указана' if self.salary_from == 0 else self.salary_from}\n"
            f"Местоположение: {self.area}\n"
            f"Ссылка на вакансию: {self.url}\n"
            f"Описание: {self.clean_search_teg(self.snippet_requirement)}\n"
            f"{self.clean_search_teg(self.snippet_responsibility)}\n-------"
        )

    def __repr__(self) -> str:
        return f"{self.to_dict()}"

    @classmethod
    def cast_to_object_list(cls, object_list: list[dict[str, Any]]) -> list["Vacancy"]:
        """Преобразование JSON файла в объект класса"""
        try:
            if not isinstance(object_list, list) or not all(isinstance(item, dict) for item in object_list):
                raise ValueError("Ожидается список словарей")
            vacancies_object = []
            for item in object_list:
                vacancy_id = item.get("id")
                name = item.get("name", "")
                area = item.get("area").get("name", "")
                salary = item.get("salary")
                if salary is None:
                    salary_from = 0
                else:
                    salary_from = item.get("salary").get("from")
                    if salary_from is None:
                        salary_from = 0
                url = item.get("alternate_url", "")
                if item.get("snippet", "").get("requirement") is None:
                    snippet_requirement = "Нет описания"
                else:
                    snippet_requirement = item.get("snippet", "").get("requirement")
                if item.get("snippet", "").get("requirement") is None:
                    snippet_responsibility = "Нет описания"
                else:
                    snippet_responsibility = item.get("snippet", "").get("requirement")
                vacancy = cls(
                    vacancy_id=vacancy_id,
                    name=name,
                    area=area,
                    salary_from=salary_from,
                    url=url,
                    snippet_requirement=snippet_requirement,
                    snippet_responsibility=snippet_responsibility,
                )
                vacancies_object.append(vacancy)
            return vacancies_object
        except Exception as e:
            print(f"Ошибка преобразования из JSON файла: {e}")

    def to_dict(self) -> dict[str, Any]:
        """Метод предоставления объекта вакансии в виде словаря"""
        return {
            "id": self.vacancy_id,
            "name": self.name,
            "area": self.area,
            "salary_from": self.salary_from,
            "url": self.url,  # [0] if isinstance(self.url, tuple) else self.url,
            "snippet_requirement": self.clean_search_teg(
                self.snippet_requirement
            ),  # [0] if isinstance(self.url, tuple) else self.snippet_requirement,
            "snippet_responsibility": self.clean_search_teg(self.snippet_responsibility),
        }

    @staticmethod
    def clean_search_teg(update_string: str) -> str:
        """Очистка поисковых тегов <highlighttext> и </highlighttext>"""
        try:
            if not isinstance(update_string, str):
                raise ValueError("Очистить от тегов можно только строку")
            clean_string = re.sub(r"<highlighttext>|</highlighttext>", "", update_string)
            return clean_string
        except Exception as e:
            print(f"Ошибка очистки тегов: {e}")
            return ""
