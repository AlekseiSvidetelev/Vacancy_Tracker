import json
import os.path
import re
from typing import Any

from config import DATA_DIR


def save_json_file(filename_json: str, vacancies: dict[str, Any]) -> None:
    """Функция для записи данных в JSON файла"""
    try:
        with open(os.path.join(DATA_DIR, filename_json), "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


def read_json_file(filename_json: str) -> dict[str, Any]:
    """Функция для чтения JSON файла в список"""
    try:
        with open(os.path.join(DATA_DIR, filename_json), "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Ошибка при чтении файла {Exception}: {e} ")
        return {}


def clean_search_teg(update_string: str) -> str:
    """Очистка поисковых тегов <highlighttext> и </highlighttext>"""
    clean_string = re.sub(r"<highlighttext>|</highlighttext>", "", update_string)
    return clean_string


def sort_vacancies(list_object, reverse=True):
    """ Функция для фильтрации списка объектов вакансий """
    try:
        sort_list_object = sorted(list_object, key=lambda x: x.salary_from, reverse=reverse)
        return sort_list_object
    except Exception as e:
        print(f"Ошибка сортировки {Exception}: {e}")


def filter_vacancies(object_list, filtered_word_list):
    """ Функция для фильтрации списка объектов вакансий по слову в описании """

    try:
        filtered_object_list = []
        pattern = re.compile('|'.join(re.escape(word) for word in filtered_word_list), flags=re.IGNORECASE)
        for object_vacancy in object_list:
            requirement = str(object_vacancy.snippet_requirement).lower()
            responsibility = str(object_vacancy.snippet_responsibility).lower()
            if pattern.search(requirement) or pattern.search(responsibility):
                filtered_object_list.append(object_vacancy)
            if not filtered_object_list:
                print("Нет вакансий под заданные критерии")
        return filtered_object_list
    except Exception as e:
        print(f"Ошибка фильтрации {Exception}: {e}")
        return []


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """ Функция для фильтрации вакансий по диапазону """
    pass


def get_top_vacancies(sorted_vacancies, top_n):
    """ Функция для выборки тов пакансий """
    pass










if __name__ == "__main__":
    # save_json_file("vacancies.json", {})
    # read_json_file("vacancies.json")
    print(
        clean_search_teg(
            "Практические навыки использования инструментов тестирования (Swagger, Postman, Fiddler/Charles, DevTools). Знакомство с Grafana. Знакомство с Kibana. Минимальные знания <highlighttext>Python</highlighttext>. ,Практические навыки использования инструментов тестирования (Swagger, Postman, Fiddler/Charles, DevTools). Знакомство с Grafana. Знакомство с Kibana. Минимальные знания <highlighttext>Python</highlighttext>."
        )
    )
    # vacancies_list = Vacancy.cast_to_object_list(list_vacancies)
    # res_sort = sort_vacancies(vacancies_list)
