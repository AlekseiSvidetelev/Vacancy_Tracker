import pytest

from src.get_vacancies_hh import HeadHunterAPI

@pytest.fixture
def test_case():
    """ Фикстура  """
    return HeadHunterAPI("vacancies.json", 250, "")

@pytest.fixture
def mock_response():
    """ Фикстура с данными get запроса на вакансии """


@pytest.fixture
def hh_api_fixture():
    """Фикстура для создания экземпляра API"""
    return HeadHunterAPI("test_vacancies.json", 100, "Python")


@pytest.fixture
def mock_api_response():
    """Фикстура с мок-ответом API"""
    return {
        "items": [
            {
                "name": "Python Developer <highlighttext>Junior</highlighttext>",
                "snippet": {"requirement": "Basic <highlighttext>Python</highlighttext>"},
                "alternate_url": "https://hh.ru/vacancy/1"
            },
            {
                "name": "Senior Python Developer",
                "snippet": {"requirement": "Advanced Python"},
                "alternate_url": "https://hh.ru/vacancy/2"
            }
        ],
        "pages": 1,
        "found": 2,
        "page": 0,
        "per_page": 100
    }
