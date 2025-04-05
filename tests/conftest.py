import pytest

from src.get_vacancies import HeadHunterAPI


@pytest.fixture
def test_case():
    return HeadHunterAPI()
