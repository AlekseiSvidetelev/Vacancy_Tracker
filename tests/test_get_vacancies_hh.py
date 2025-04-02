import pytest
from unittest.mock import patch
import requests

from src.get_vacancies import HeadHunterAPI


@pytest.fixture
def test_case():
    return HeadHunterAPI(file_worker="vacancies.json", number_vacancies=150)

@patch('requests.get')
def test_get_vacancies_hh_success(mock_get, test_case, capsys):
    """Тест успешного получения вакансий"""
    mock_response = {'items': [{'id': 1}, {'id': 2}], 'pages': 1}
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 200
    test_case.get_vacancies_hh("Python")
    assert len(test_case.vacancies) == 2
    assert test_case.vacancies == [{'id': 1}, {'id': 2}]
    mock_get.assert_any_call(test_case.url, headers=test_case.headers,
                                         params={'text': 'Python', 'page': 0, 'per_page': 100})
    repr(test_case)
    captured = capsys.readouterr()
    assert captured.out == ""
    str(test_case)
    captured = capsys.readouterr()
    assert captured.out == ""


@patch('requests.get')
def test_get_vacancies_hh_connection_error(mock_get, test_case, capsys):
    mock_response = {'items': [{'id': 1}, {'id': 2}], 'pages': 1}
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 400
    test_case.get_vacancies_hh("Python")
    captured = capsys.readouterr()
    assert captured.out == ('Нет подключения к API. Загрузка прервана.\n'
                            "Ошибка при получении данных <class 'Exception'>: Нет подключения к API. "
                            'Загрузка прервана.\n')

