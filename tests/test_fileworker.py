import json
import os

from config import DATA_DIR
from src.fileworker import JSONSaver

from src.vacancy_operations import Vacancy


def test_class_jsonsaver(test_list_hh, test_data):
    """ Проверка работы класса JSONSaver """
    vacancy_list = Vacancy.cast_to_object_list(test_list_hh)
    file_name = "testing.json"
    res_1 = JSONSaver(file_name)
    assert res_1.file_name == file_name
    assert repr(res_1) == file_name
    for vacavcy in vacancy_list:
        res_1.save_to_file(vacavcy)
    with open(os.path.join(DATA_DIR, file_name), "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    assert loaded_data == test_data
    for vacavcy in vacancy_list:
        res_1.deleting_from_file(vacavcy)
    with open(os.path.join(DATA_DIR, file_name), "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    assert loaded_data == []


def test_exception_add(test_list_hh, capsys):
    """ Проверка исключений и вывод информации в консоль JSONSaver при сохранении """
    res_1 = JSONSaver()
    res_1.save_to_file("123")
    captured = capsys.readouterr()
    assert captured.out == (
        "Ошибка при добавлении вакансии в файл: В файл можно "
        "добавлять только объекты класса Vacancy или его наследников\n"
    )


def test_exception_del(test_list_hh, capsys):
    """ Проверка исключений и вывод информации в консоль JSONSaver при удалении """
    res_1 = JSONSaver()
    res_1.deleting_from_file("123")
    captured = capsys.readouterr()
    assert captured.out == (
        "Ошибка при удалении вакансии: В файле можно удалять только объекты класса " "Vacancy или его наследников\n"
    )
