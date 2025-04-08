from src.get_vacancies import HeadHunterAPI
from unittest.mock import patch, Mock


@patch("requests.get")
def test_class_hh(mock_requests_get):
    """Тест успешного получения вакансий с несколькими страницами"""
    mock_responses = [
        {"items": [{"id": 1}, {"id": 2}], "found": 10, "pages": 2},
        {"items": [{"id": 3}, {"id": 4}], "found": 10, "pages": 2},
        {"items": [], "found": 0, "pages": 2},
    ]
    mock_requests_get.side_effect = [
        Mock(status_code=200, json=lambda: mock_responses[0]),
        Mock(status_code=200, json=lambda: mock_responses[1]),
        Mock(status_code=200, json=lambda: mock_responses[2]),
    ]
    hh_api = HeadHunterAPI()
    hh_api.get_vacancies("тестировщик")

    assert hh_api.vacancies == [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}]
    assert repr(hh_api) == "HeadHunterAPI. Получено вакансий: 4, Время запроса: 0.5"
    assert str(hh_api) == "[{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]"


@patch("requests.get")
def test_class_hh_exception(mock_requests_get, capsys):
    """Тест ошибки подключения"""
    mock_requests_get.side_effect = [Mock(status_code=404)]
    hh_api = HeadHunterAPI()
    hh_api.get_vacancies("тестировщик")

    assert hh_api.vacancies == []
    captured = capsys.readouterr()
    assert captured.out == (
        "Нет соединения с сервисом API для получения данных\n"
        "Ошибка <class 'Exception'>: Нет соединения с сервисом API для получения "
        "данных\n"
        "Ошибка при получении вакансий: 'NoneType' object has no attribute 'json'\n"
    )
