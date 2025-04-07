import json
import os.path
import re
from typing import Any

from config import DATA_DIR


def clean_search_teg(update_string: str) -> str:
    """Очистка поисковых тегов <highlighttext> и </highlighttext>"""
    clean_string = re.sub(r"<highlighttext>|</highlighttext>", "", update_string)
    return clean_string

# def update_tuple_in_str(update_string: str)



def sort_vacancies(list_object, reverse=True):
    """Функция для фильтрации списка объектов вакансий"""
    try:
        sort_list_object = sorted(list_object, key=lambda x: x.salary_from, reverse=reverse)
        return sort_list_object
    except Exception as e:
        print(f"Ошибка сортировки {Exception}: {e}")


def filter_vacancies(object_list, filtered_word_list):
    """Функция для фильтрации списка объектов вакансий по слову в описании"""

    try:
        filtered_object_list = []
        pattern = re.compile("|".join(re.escape(word) for word in filtered_word_list), flags=re.IGNORECASE)
        for object_vacancy in object_list:
            requirement = str(object_vacancy.snippet_requirement).lower()
            responsibility = str(object_vacancy.snippet_responsibility).lower()
            if pattern.search(requirement) or pattern.search(responsibility):
                filtered_object_list.append(object_vacancy)
        return filtered_object_list
    except Exception as e:
        print(f"Ошибка фильтрации {Exception}: {e}")
        return []


def get_vacancies_by_salary(filtered_vacancies, salary_range=None):
    """Функция для фильтрации вакансий по диапазону"""
    if salary_range is None:
        print("Критерии диапазона выборки не заданы")
        return filtered_vacancies
    try:
        parts = salary_range.replace(" ", "").split("-")
        lower_salary = int(parts[0])
        upper_salary = int(parts[1]) if len(parts) > 1 else None
        if upper_salary is None:
            return [vacancy for vacancy in filtered_vacancies if lower_salary <= vacancy.salary_from]
        filtered_object_list = [
            vacancy for vacancy in filtered_vacancies if (lower_salary <= vacancy.salary_from <= upper_salary)
        ]
        return filtered_object_list
    except Exception as e:
        print(f"Ошибка {Exception} при попытке получения выборки: {e}")
        return []


def get_top_vacancies(sorted_vacancies, top_n):
    """Функция для выборки Топ-N вакансий"""
    try:
        if type(top_n) != int:
            raise ValueError("Значение должно быть целым числом")
        return sorted_vacancies[:top_n]
    except Exception as e:
        print(f"Ошибка {Exception} формирования топ - {top_n} вакансий: {e}")
        return []


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
