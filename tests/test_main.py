import pytest

from src.get_vacancies import HeadHunterAPI
from src.vacancy_operations import Vacancy
from src.utils import sort_vacancies, get_vacancies_by_salary, get_top_vacancies, filter_vacancies


def test_user_interaction(test_list_hh, capsys):
    hh_vacancies = Vacancy.cast_to_object_list(test_list_hh)
    assert repr(hh_vacancies) == (
        "[{'id': '115882074', 'name': 'Ученик на производство', 'area': 'Фрязино "
        "(Московская область)', 'salary_from': 0, 'url': "
        "'https://hh.ru/vacancy/115882074', 'snippet_requirement': 'Образование не "
        "ниже средне-специального. Внимательность. Усидчивость. Готовность работать в "
        "сменном графике.', 'snippet_responsibility': 'Образование не ниже "
        "средне-специального. Внимательность. Усидчивость. Готовность работать в "
        "сменном графике.'}, {'id': '118448461', 'name': 'Откачник-вакуумщик 4 "
        "разряда', 'area': 'Санкт-Петербург', 'salary_from': 0, 'url': "
        "'https://hh.ru/vacancy/118448461', 'snippet_requirement': 'Среднее "
        "профессиональное образование. Аккуратность, ответственность.', "
        "'snippet_responsibility': 'Среднее профессиональное образование. "
        "Аккуратность, ответственность.'}, {'id': '118832907', 'name': "
        "'Вакуумщик/Оператор вакуумного станка', 'area': 'Костанай', 'salary_from': "
        "300000, 'url': 'https://hh.ru/vacancy/118832907', 'snippet_requirement': "
        "'Нет описания', 'snippet_responsibility': 'Нет описания'}]"
    )
    hh_vacancies = Vacancy.cast_to_object_list("test_list_hh")
    captured = capsys.readouterr()
    assert captured.out == 'Ошибка преобразования из JSON файла: Ожидается список словарей\n'


def test_filter_vacancies(test_list_hh, capsys):
    """ Тест функции фильтрации """
    hh_vacancies = Vacancy.cast_to_object_list(test_list_hh)
    filtered_vacancies = filter_vacancies(hh_vacancies, "усидчивость")
    assert repr(filtered_vacancies) == ("[{'id': '115882074', 'name': 'Ученик на производство', 'area': 'Фрязино "
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
    filtered_vacancies = filter_vacancies(hh_vacancies, True)
    captured = capsys.readouterr()
    assert captured.out == "Ошибка фильтрации <class 'Exception'>: 'bool' object is not iterable\n"


def test_get_vacancies_by_salary(test_list_hh, capsys):
    """ Тест функции получения выборки по зарплате """
    hh_vacancies = Vacancy.cast_to_object_list(test_list_hh)
    ranged_vacancies = get_vacancies_by_salary(hh_vacancies, "200000")
    assert repr(ranged_vacancies) == ("[{'id': '118832907', 'name': 'Вакуумщик/Оператор вакуумного станка', 'area': "
                                     "'Костанай', 'salary_from': 300000, 'url': 'https://hh.ru/vacancy/118832907', "
                                     "'snippet_requirement': 'Нет описания', 'snippet_responsibility': 'Нет "
                                     "описания'}]")
    ranged_vacancies = get_vacancies_by_salary(hh_vacancies, "sdfs")
    captured = capsys.readouterr()
    assert captured.out == ("Ошибка <class 'Exception'> при попытке получения выборки: invalid literal "
                            "for int() with base 10: 'sdfs'\n")

def test_sort_vacancies(test_list_hh, capsys):
    """ Тест функции сортировки объекта вакансий """
    hh_vacancies = Vacancy.cast_to_object_list(test_list_hh)
    sorted_vacancies = sort_vacancies(hh_vacancies, False)
    assert repr(sorted_vacancies) == ("[{'id': '115882074', 'name': 'Ученик на производство', 'area': 'Фрязино "
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
    sorted_vacancies = sort_vacancies(hh_vacancies, 123)
    captured = capsys.readouterr()
    assert captured.out == ("Ошибка сортировки <class 'Exception'>: Проверьте данные для направления "
                                'сортировки\n')

def test_get_top_vacancies(test_list_hh, capsys):
    """ Тестирование выборки топ вакансий """
    hh_vacancies = Vacancy.cast_to_object_list(test_list_hh)
    top_vacancy = get_top_vacancies(hh_vacancies, 1)
    assert repr(top_vacancy) == ("[{'id': '115882074', 'name': 'Ученик на производство', 'area': 'Фрязино "
                                 "(Московская область)', 'salary_from': 0, 'url': "
                                 "'https://hh.ru/vacancy/115882074', 'snippet_requirement': 'Образование не "
                                 'ниже средне-специального. Внимательность. Усидчивость. Готовность работать в '
                                 "сменном графике.', 'snippet_responsibility': 'Образование не ниже "
                                 'средне-специального. Внимательность. Усидчивость. Готовность работать в '
                                 "сменном графике.'}]")
    top_vacancy = get_top_vacancies(hh_vacancies, "123")
    captured = capsys.readouterr()
    assert captured.out == ("Ошибка <class 'Exception'> формирования топ - 123 вакансий: введите целое "
                            'число для выборки топ вакансий\n')



