import json
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from config import DATA_DIR
from src.vacancy_operations import Vacancy


class Saver(ABC):

    file_name: str

    @abstractmethod
    def __init__(self, file_name):
        self.__file_name = file_name


    @abstractmethod
    def read_to_file(self, file_name: str):
        pass

    @abstractmethod
    def save_to_file(self, vacancy: Vacancy) -> None:
        pass

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value


class JSONSaver(Saver):

    def __init__(self, file_name = ""):
        super().__init__(file_name if file_name else "vacancies.json")
        self.__file_name = file_name if file_name else "vacancies.json"

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, new_file_name: str) -> None:
        try:
            if new_file_name[-5:]  == ".json":
                print("Необходимо создать название файла с расширением '.json'")
                raise ValueError("Неправильный формат файла")
            self.__file_name = new_file_name
        except Exception as e:
            print(f"Ошибка {Exception}: {e}")

    def read_to_file(self, file_name: str) -> dict[str, Any]:
        """Функция для чтения JSON файла в список"""
        try:
            with open(os.path.join(DATA_DIR, self.__file_name), "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Ошибка при чтении файла {Exception}: {e} ")
            return {}

    def save_to_file(self, vacancy: Vacancy) -> None:
        """Функция для записи данных в JSON файл"""
        try:
            print(self.__file_name)
            if not isinstance(vacancy, Vacancy):
                raise TypeError("В категорию можно добавлять только объекты класса Vacancy или его наследников")
            Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
            if not os.path.exists(self.__file_name):
                with open(os.path.join(DATA_DIR, self.__file_name), "w", encoding="utf-8") as f:
                    json.dumps(f)
            with open(os.path.join(DATA_DIR, self.__file_name), "r", encoding="utf-8") as f:
                old_vacancies = json.load(f)
            if not old_vacancies:
                old_vacancies = []
            new_vacancy = vacancy.to_dict()
            for old_vacancy in old_vacancies:
                if old_vacancy["id"] == new_vacancy["id"]:
                    return
                old_vacancies.append(new_vacancy)
            with open(os.path.join(DATA_DIR, self.__file_name), "w", encoding="utf-8") as f:
                json.dump(old_vacancies, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка {Exception} при добавлении вакансии в файл: {e}")

