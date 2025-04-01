import json
import os.path

from config import DATA_DIR



def save_json_file(filename_json: str, vacancies):
    """ Функция для чтения JSON файла """
    try:
        with open(os.path.join(DATA_DIR, filename_json), 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")



if __name__ == "__main__":
    print(save_json_file("vacancies.json"))