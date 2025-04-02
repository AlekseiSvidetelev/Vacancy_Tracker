from unittest.mock import patch, Mock


def test_init_class(test_case):
    assert test_case.file_worker == "vacancies.json"
    assert test_case.number_vacancies == 250
    assert test_case.search_word == ""



@patch('requests.get')
def test_successful_vacancy_fetching(mock_get, hh_api_fixture, mock_api_response):
    """Тест успешного получения вакансий"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_response
    mock_get.return_value = mock_response
    hh_api_fixture.get_vacancies_hh("Python")
    assert len(hh_api_fixture.vacancies) == 2


@patch('src.get_vacancies_hh.save_json_file')
def test_save_to_json(mock_save, hh_api_fixture, mock_api_response):
    """Тест сохранения в JSON"""
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_api_response
        mock_get.return_value = mock_response

        hh_api_fixture.get_vacancies_hh("Python")
        hh_api_fixture.save_to_json()

    mock_save.assert_called_once_with(
        "test_vacancies.json",
        {
            "items": hh_api_fixture.vacancies,
            "found": len(hh_api_fixture.vacancies),
            "pages": 1,
            "page": 0,
            "per_page": 100,
            "alternate_url": "https://hh.ru/search/vacancy?text=Python"
        }
    )
