import json
import os

from config import DATA_DIR
from src.fileworker import JSONSaver

from src.vacancy_operations import Vacancy

def test_class_jsonsaver(test_list_hh, test_data):
    vacancy_list = Vacancy.cast_to_object_list(test_list_hh)
    file_name = "vacancies.json"
    res_1 = JSONSaver()
    assert res_1.file_name == file_name
    assert repr(res_1) == file_name
    for vacavcy in vacancy_list:
        res_1.save_to_file(vacavcy)
    with open(os.path.join(DATA_DIR, file_name), 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    assert loaded_data == test_data, "Данные в файле не соответствуют ожидаемым"
    for vacavcy in vacancy_list:
        res_1.deleting_from_file(vacavcy)
    with open(os.path.join(DATA_DIR, file_name), 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    assert loaded_data == []

def test_exception_add(test_list_hh, capsys):
    res_1 = JSONSaver()
    res_1.save_to_file("123")
    captured = capsys.readouterr()
    assert captured.out == ("Ошибка при добавлении вакансии в файл: В файл можно "
                            'добавлять только объекты класса Vacancy или его наследников\n')

def test_exception_del(test_list_hh, capsys):
    res_1 = JSONSaver()
    res_1.deleting_from_file("123")
    captured = capsys.readouterr()
    assert captured.out == ('Ошибка при удалении вакансии: В файле можно удалять только объекты класса '
                            'Vacancy или его наследников\n')
