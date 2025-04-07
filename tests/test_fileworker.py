from src.fileworker import JSONSaver

from src.vacancy_operations import Vacancy

def test_class_jsonsaver(test_list_hh):
    vacancy_list = Vacancy.cast_to_object_list(test_list_hh)
    res_1 = JSONSaver("vacancies_test")
    assert res_1.file_name == 'vacancies_test.json'
    res_2 = JSONSaver("test")
    assert res_2.file_name == "test.json"
    assert repr(res_2) == "test.json"
    for vacavcy in vacancy_list:
        res_1.save_to_file(vacavcy)

        # Проверка существования файла
        # assert file_path.exists(), "Файл не был создан"

        # # Проверка содержимого файла
        # with open(file_path, 'r', encoding='utf-8') as f:
        #     loaded_data = json.load(f)
        #
        # assert loaded_data == test_data, "Данные в файле не соответствуют ожидаемым"



# def test_write_json_to_file(tmp_path: Path):
#     # Подготовка тестовых данных
#     test_data = {"name": "Alice", "age": 30, "hobbies": ["reading", "travel"]}
#     file_path = tmp_path / "test_data.json"
#
#     # Вызов тестируемой функции
#     JSONSaver.save_to_file(test_data, file_path)
#
#     # Проверка существования файла
#     assert file_path.exists(), "Файл не был создан"
#
#     # Проверка содержимого файла
#     with open(file_path, 'r', encoding='utf-8') as f:
#         loaded_data = json.load(f)
#
#     assert loaded_data == test_data, "Данные в файле не соответствуют ожидаемым"

