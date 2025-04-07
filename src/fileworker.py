import json
import os
import re
from abc import ABC, abstractmethod
from typing import Any

from config import DATA_DIR
from src.vacancy_operations import Vacancy


class Saver(ABC):

    file_name: str

    @abstractmethod
    def __init__(self, file_name):
        self.file_name = file_name

    @property
    @abstractmethod
    def file_name(self) -> str:
        pass

    @file_name.setter
    @abstractmethod
    def file_name(self, value: str) -> None:
        pass

    @abstractmethod
    def read_from_file(self, file_name: str) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def save_to_file(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def deleting_from_file(self, vacancy: Vacancy) -> None:
        pass


class JSONSaver(Saver):

    def __init__(self, file_name: str = None):
        super().__init__(file_name)
        self.file_name = file_name if file_name else "vacancies.json"

    def __repr__(self):
        return f"{self.file_name}"

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, new_file_name: str) -> None:
        try:
            clean_word = re.sub(r'[<>:"/\\|?*]', "", new_file_name)
            replace_spase = clean_word.replace(" ", "_")
            parts_name = replace_spase.split(".")
            self._file_name = parts_name[0] + ".json"
        except Exception as e:
            print(f"Ошибка {Exception}: {e}")

    def read_from_file(self, file_name: str) -> list[dict[str, Any]]:
        """Функция для чтения JSON файла"""
        try:
            if not os.path.exists(os.path.join(DATA_DIR, self.file_name)):
                with open(os.path.join(DATA_DIR, self.file_name), "w", encoding="utf-8") as f:
                    json.dump([], f)
            with open(os.path.join(DATA_DIR, self.file_name), "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Ошибка при чтении файла {Exception}: {e} ")
            return []

    def save_to_file(self, vacancy: Vacancy) -> None:
        """Функция для записи данных в JSON файл"""
        try:
            if not isinstance(vacancy, Vacancy):
                raise TypeError("В файл можно добавлять только объекты класса Vacancy или его наследников")
            old_vacancies = self.read_from_file(self.file_name)
            new_vacancy = vacancy.to_dict()
            if old_vacancies == []:
                with open(os.path.join(DATA_DIR, self.file_name), "w", encoding="utf-8") as f:
                    json.dump(old_vacancies, f, ensure_ascii=False, indent=4)
            for old_vacancy in old_vacancies:
                if old_vacancy["id"] == new_vacancy["id"]:
                    return
                old_vacancies.append(new_vacancy)
            with open(os.path.join(DATA_DIR, self.file_name), "w", encoding="utf-8") as f:
                json.dump(old_vacancies, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка {Exception} при добавлении вакансии в файл: {e}")

    def deleting_from_file(self, vacancy: Vacancy) -> None:
        """Функция для записи данных в JSON файл"""
        try:
            if not isinstance(vacancy, Vacancy):
                raise TypeError("В файле можно удалять только объекты класса Vacancy или его наследников")
            old_vacancies = self.read_from_file(self.file_name)
            new_vacancy = vacancy.to_dict()
            for old_vacancy in old_vacancies:
                if old_vacancy["id"] == new_vacancy["id"]:
                    old_vacancies.remove(new_vacancy)
            with open(os.path.join(DATA_DIR, self.file_name), "w", encoding="utf-8") as f:
                json.dump(old_vacancies, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при удалении вакансии: {e}")


if __name__ == "__main__":
    saver = JSONSaver("vac.json")
    print(saver)
    # saver.file_name = "file.txt"
    # print(saver.file_name)
    # saver.file_name = "filesefd.refl.erfe"
    # print(saver.file_name)
    # saver.file_name = "file.rtg"
    # print(saver.file_name)
    # saver.file_name = "file><jg"
    # print(saver.file_name)
    # saver.file_name = "asd_asd.asd"
    # print(saver.file_name)
