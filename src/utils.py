import re


def clean_split_str(update_str: str) -> list[str]:
    """ Убирает символы из строки и разделяет по пробелу """
    try:
        if not isinstance(update_str, str):
            raise ValueError("Запрос не является строкой")
        clean_update_str = (re.sub(r'[^\w\s]', '', update_str)).lower()
        word_list = clean_update_str.split()
        return word_list
    except Exception as e:
        print(f"Ошибка преобразования слов фильтрации: {e}")


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


def sort_vacancies(list_object: list[object], reverse=True) -> list[object]:
    """Функция для фильтрации списка объектов вакансий"""
    try:
        if not isinstance(reverse, bool):
            raise ValueError("Проверьте данные для направления сортировки")
        sort_list_object = sorted(list_object, reverse=reverse)
        return sort_list_object
    except Exception as e:
        print(f"Ошибка сортировки {Exception}: {e}")


def filter_vacancies(object_list: object, filtered_list):
    """Функция для фильтрации списка объектов вакансий по слову в описании"""
    try:
        if not isinstance(filtered_list, list):
            raise ValueError("Для фильтрации введите слова")
        filtered_object_list = []
        pattern = re.compile("(" + "|".join(map(re.escape, filtered_list)) + ")", flags=re.IGNORECASE)
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


def get_top_vacancies(vacancies, top_n):
    """Функция для выборки Топ-N вакансий"""
    try:
        if not isinstance(top_n, int):
            raise ValueError("Введите целое число для выборки топ вакансий")
        return vacancies[:top_n]
    except Exception as e:
        print(f"Ошибка {Exception} формирования топ - {top_n} вакансий: {e}")
        return []


if __name__ == "__main__":
    # save_json_file("vacancies.json", {})
    # read_json_file("vacancies.json")
    # print(
    #     clean_search_teg(
    #         "Практические навыки использования инструментов тестирования (Swagger,
    #         Postman, Fiddler/Charles, DevTools). Знакомство с Grafana. Знакомство с Kibana.
    #         Минимальные знания <highlighttext>Python</highlighttext>. ,Практические навыки
    #         использования инструментов тестирования (Swagger, Postman, Fiddler/Charles, DevTools).
    #         Знакомство с Grafana. Знакомство с Kibana. Минимальные знания <highlighttext>Python</highlighttext>."
    #     )
    # )
    print(
        filter_vacancies(
            "Практические навыки использования инструментов тестирования "
            "(Swagger, Postman, Fiddler/Charles, DevTools). Знакомство с Grafana. "
            "Знакомство с Kibana. Минимальные знания <highlighttext>Python</highlighttext>. "
            ",Практические навыки использования инструментов тестирования (Swagger, Postman, "
            "Fiddler/Charles, DevTools). Знакомство с Grafana. Знакомство с Kibana. Минимальные "
            "знания <highlighttext>Python</highlighttext>.",
            "kibana",
        )
    )
    # vacancies_list = Vacancy.cast_to_object_list(list_vacancies)
    # res_sort = sort_vacancies(vacancies_list)
