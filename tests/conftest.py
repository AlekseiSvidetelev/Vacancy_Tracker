import pytest

from src.get_vacancies import HeadHunterAPI


@pytest.fixture
def test_case():
    return HeadHunterAPI(file_worker="vacancies.json", number_vacancies=150)
