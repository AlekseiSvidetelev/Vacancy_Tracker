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


if __name__ == "__main__":
    # save_json_file("vacancies.json", {})
    # read_json_file("vacancies.json")
    print(
        clean_search_teg(
            "Практические навыки использования инструментов тестирования (Swagger, Postman, Fiddler/Charles, DevTools). Знакомство с Grafana. Знакомство с Kibana. Минимальные знания <highlighttext>Python</highlighttext>. ,Практические навыки использования инструментов тестирования (Swagger, Postman, Fiddler/Charles, DevTools). Знакомство с Grafana. Знакомство с Kibana. Минимальные знания <highlighttext>Python</highlighttext>."
        )
    )
