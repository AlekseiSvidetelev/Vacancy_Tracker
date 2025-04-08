import time

from src.get_vacancies import HeadHunterAPI
from src.vacancy_operations import Vacancy
from src.fileworker import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_vacancies_by_salary, get_top_vacancies


# hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies()

    # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer",
#                   "<https://hh.ru/vacancy/123456>",
#                   "100 000-150 000 руб.",
#                   "Требования: опыт работы от 3 лет...")

    # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)

    # Функция для взаимодействия с пользователем
def user_interaction():
    """ Функция для взаимодействия с пользователем """
    try:
        platforms = ["HeadHunter"]
        search_query = input(f"Введите поисковый запрос {platforms}: ")
        print("Выполняется поиск. Ждите...")
        hh_api = HeadHunterAPI()
        hh_vacancies = hh_api.get_vacancies(search_query)
        if not hh_vacancies:
            raise ValueError("Вакансий с заданными параметрами не найдено")
        vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
        print(f"Найдено вакансий: {len(vacancies_list)}.")
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        if not filtered_vacancies:
            raise ValueError("Вакансий с заданными параметрами не найдено")
        print(f"Количество вакансий под ключевые критерии: {len(filtered_vacancies)}")
        salary_range = input("Введите диапазон зарплат (Пример: '100000 - 150000' или '100000'): ") # Пример: 100000 - 150000
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        if not ranged_vacancies:
            raise ValueError("Вакансий с заданными параметрами не найдено")
        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        if not top_vacancies:
            raise ValueError("Вакансий с заданными параметрами не найдено")
        json_saver = JSONSaver()
        for vacancy in top_vacancies:
            json_saver.save_to_file(vacancy)
            print(vacancy)
    except Exception as e:
        print(f"Ошибка работы программы: {e}")




if __name__ == "__main__":
    user_interaction()
