from unittest.mock import patch


@patch("requests.get")
def test_get_vacancies_hh_success(mock_get, test_case, capsys):
    """Тест успешного получения вакансий и записи в файл"""
    mock_response = {"items": [{"id": 1}, {"id": 2}], "pages": 1}
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 200
    test_case.get_vacancies_hh("Python")
    assert len(test_case.vacancies) == 2
    assert test_case.vacancies == [{"id": 1}, {"id": 2}]
    mock_get.assert_any_call(
        test_case.url, headers=test_case.headers, params={"text": "Python", "page": 0, "per_page": 100}
    )
    test_case.save_to_json()
    repr(test_case)
    captured = capsys.readouterr()
    assert captured.out == "Данные успешно записаны в файл: vacancies.json\n"


@patch("requests.get")
def test_save_json_exception(mock_get, test_case, capsys):
    """Тест записи пустого списка вакансий"""
    mock_response = {"items": [], "pages": 1}
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 200
    test_case.get_vacancies_hh("Python")
    assert len(test_case.vacancies) == 0
    assert test_case.vacancies == []
    mock_get.assert_any_call(
        test_case.url, headers=test_case.headers, params={"text": "Python", "page": 0, "per_page": 100}
    )
    test_case.save_to_json()
    str(test_case)
    captured = capsys.readouterr()
    assert captured.out == (
        "Список вакансий для записи пустой\n"
        "Ошибка '<class 'Exception'>' при сохранении файла: Нет данных для записи\n"
    )


@patch("requests.get")
def test_get_vacancies_hh(mock_get, test_case, capsys):
    """Тест ошибки подключения"""
    mock_response = {"items": [], "pages": 1}
    mock_get.return_value.json.return_value = mock_response
    mock_get.return_value.status_code = 404
    test_case.get_vacancies_hh("Python")
    captured = capsys.readouterr()
    assert captured.out == (
        "Ошибка подключения: \n"
        "Нет подключения к API. Загрузка прервана.\n"
        "Ошибка при получении данных <class 'Exception'>: Нет подключения к API. "
        "Загрузка прервана.\n"
    )
