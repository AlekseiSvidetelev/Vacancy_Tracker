from src.vacancy_operations import Vacancy


def test_class_vacancy(test_list_hh):
    """Проверка класса Vacancy"""
    vacancy_list = Vacancy.cast_to_object_list(test_list_hh)
    assert repr(vacancy_list) == (
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
    assert len(vacancy_list) == 3
    assert vacancy_list[0].vacancy_id == "115882074"
    assert vacancy_list[1].vacancy_id == "118448461"
    assert vacancy_list[2].vacancy_id == "118832907"
    assert vacancy_list[0].to_dict() == {
        "area": "Фрязино (Московская область)",
        "id": "115882074",
        "name": "Ученик на производство",
        "salary_from": 0,
        "snippet_requirement": "Образование не ниже средне-специального. "
        "Внимательность. Усидчивость. Готовность работать в "
        "сменном графике.",
        "snippet_responsibility": "Образование не ниже средне-специального. "
        "Внимательность. Усидчивость. Готовность работать в "
        "сменном графике.",
        "url": "https://hh.ru/vacancy/115882074",
    }
    assert vacancy_list[0].salary_from == 0
    assert vacancy_list[1].salary_from == 0
    assert vacancy_list[2].salary_from == 300000
    assert str(vacancy_list[0]) == (
        "ID: 115882074\n"
        "Название вакансии: Ученик на производство\n"
        "Зарплата от: не указана\n"
        "Местоположение: Фрязино (Московская область)\n"
        "Ссылка на вакансию: https://hh.ru/vacancy/115882074\n"
        "Описание: Образование не ниже средне-специального. Внимательность. "
        "Усидчивость. Готовность работать в сменном графике.\n"
        "Образование не ниже средне-специального. Внимательность. Усидчивость. "
        "Готовность работать в сменном графике.\n"
        "-------"
    )
