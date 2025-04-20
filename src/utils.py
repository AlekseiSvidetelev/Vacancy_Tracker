import re
from typing import Optional

from src.vacancy_operations import Vacancy


def clean_split_str(update_str: str) -> list[str]:
    """Убирает символы из строки и разделяет по пробелу"""
    try:
        if not isinstance(update_str, str):
            raise ValueError("Запрос не является строкой")
        clean_update_str = (re.sub(r"[^\w\s]", "", update_str)).lower()
        word_list = clean_update_str.split()
        return word_list
    except Exception as e:
        print(f"Ошибка преобразования слов фильтрации: {e}")


def sort_vacancies(list_object: list["Vacancy"], reverse=True) -> list["Vacancy"]:
    """Функция для фильтрации списка объектов вакансий"""
    try:
        if not isinstance(reverse, bool):
            raise ValueError("Проверьте данные для направления сортировки")
        sort_list_object = sorted(list_object, reverse=reverse)
        return sort_list_object
    except Exception as e:
        print(f"Ошибка сортировки {Exception}: {e}")


def filter_vacancies(object_list: list["Vacancy"], filtered_list: list[str]) -> list["Vacancy"]:
    """Функция для фильтрации списка объектов вакансий по слову в описании"""
    try:
        if not isinstance(filtered_list, list):
            raise ValueError("Для фильтрации введите слова")
        filtered_object_list = []
        pattern = re.compile(".*(" + "|".join(map(re.escape, filtered_list)) + ").*", flags=re.IGNORECASE)
        for object_vacancy in object_list:
            requirement = str(object_vacancy.snippet_requirement).lower()
            responsibility = str(object_vacancy.snippet_responsibility).lower()
            combined_text = f"{requirement} {responsibility}"
            if pattern.search(combined_text):
                filtered_object_list.append(object_vacancy)
        return filtered_object_list
    except Exception as e:
        print(f"Ошибка фильтрации {Exception}: {e}")
        return []


def get_vacancies_by_salary(
    filtered_vacancies: list["Vacancy"], salary_range: Optional[str] = None
) -> list["Vacancy"]:
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
        print(f"Ошибка при попытке получения выборки вакансий: {e}")
        return []


def get_top_vacancies(vacancies_list: list["Vacancy"], top_n: int) -> list["Vacancy"]:
    """Функция для выборки Топ-N вакансий"""
    try:
        if not isinstance(top_n, int):
            raise ValueError("Введите целое число для выборки топ вакансий")
        return vacancies_list[:top_n]
    except Exception as e:
        print(f"Ошибка {Exception} формирования топ - {top_n} вакансий: {e}")
        return []
