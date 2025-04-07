from src.get_vacancies import HeadHunterAPI
from src.vacancy_operations import Vacancy
from src.utils import sort_vacancies, get_vacancies_by_salary, get_top_vacancies, filter_vacancies


def test_user_interaction(test_list_hh):
    hh_vacancies = Vacancy.cast_to_object_list(test_list_hh)
    assert repr(hh_vacancies) == ("[{'id': '115882074', 'name': 'Ученик на производство', 'area': 'Фрязино "
                                 "(Московская область)', 'salary_from': 0, 'url': "
                                 "'https://hh.ru/vacancy/115882074', 'snippet_requirement': 'Образование не "
                                 'ниже средне-специального. Внимательность. Усидчивость. Готовность работать в '
                                 "сменном графике.', 'snippet_responsibility': 'Образование не ниже "
                                 'средне-специального. Внимательность. Усидчивость. Готовность работать в '
                                 "сменном графике.'}, {'id': '118448461', 'name': 'Откачник-вакуумщик 4 "
                                 "разряда', 'area': 'Санкт-Петербург', 'salary_from': 0, 'url': "
                                 "'https://hh.ru/vacancy/118448461', 'snippet_requirement': 'Среднее "
                                 "профессиональное образование. Аккуратность, ответственность.', "
                                 "'snippet_responsibility': 'Среднее профессиональное образование. "
                                 "Аккуратность, ответственность.'}, {'id': '118832907', 'name': "
                                 "'Вакуумщик/Оператор вакуумного станка', 'area': 'Костанай', 'salary_from': "
                                 "300000, 'url': 'https://hh.ru/vacancy/118832907', 'snippet_requirement': "
                                 "'Нет описания', 'snippet_responsibility': 'Нет описания'}]")
    filtered_vacancies = filter_vacancies(hh_vacancies, "усидчивость")
    assert repr(filtered_vacancies) == ""