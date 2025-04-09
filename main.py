from src.fileworker import JSONSaver
from src.get_vacancies import HeadHunterAPI
from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, sort_vacancies, clean_split_str
from src.vacancy_operations import Vacancy


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""
    try:
        # Формирование поискового запроса от пользователя
        platforms = ["HeadHunter"]
        search_query = input(f"Введите поисковый запрос {platforms}: ")
        print("Выполняется поиск. Ждите...")

        # Запрос API
        hh_api = HeadHunterAPI()
        hh_vacancies = hh_api.get_vacancies(search_query)
        if not hh_vacancies:
            raise ValueError("Вакансий с заданными параметрами не найдено")

        # Преобразование списка вакансий в объекты вакансий
        vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
        print(f"Найдено вакансий: {len(vacancies_list)}.")

        # Фильтрация вакансий по заданным параметрам
        filter_words = clean_split_str(input("Введите ключевые слова для фильтрации вакансий: "))
        print(filter_words)
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        if not filtered_vacancies:
            raise ValueError("Вакансий с заданными параметрами не найдено")
        print(f"Количество вакансий под ключевые критерии: {len(filtered_vacancies)}")

        # Выборка по заработной плате. Можно указать диапазон, а можно указать одно значение от -
        salary_range = input(
            "Введите диапазон зарплат (Пример: '100000 - 150000' или '100000'): "
        )  # Пример: 100000 - 150000
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        if not ranged_vacancies:
            raise ValueError("Вакансий с заданными параметрами не найдено")

        # Сортировка вакансий по заработной плате. По умолчанию сортируется от большего к меньшему
        sorted_vacancies = sort_vacancies(ranged_vacancies)

        # Формирование топ вакансий
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        if not top_vacancies:
            raise ValueError("Вакансий с заданными параметрами не найдено")

        # Сохранение вакансий в JSON файл
        json_saver = JSONSaver()
        for vacancy in top_vacancies:
            json_saver.save_to_file(vacancy)
            print(vacancy)
        print("END")
    except Exception as e:
        print(f"Ошибка работы программы: {e}")


if __name__ == "__main__":
    user_interaction()
