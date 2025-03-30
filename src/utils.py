import json
import os.path

from config import DATA_DIR



def load_json_file(filname: str, vacancies):
    """ Функция для чтения JSON файла """
    try:
        # with open(os.path.join(DATA_DIR, filname), "r", encoding = "utf-8") as f:
        #     return json.load(f)
        with open(os.path.join(DATA_DIR, filname), 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


if __name__ == "__main__":
    print(load_json_file("vacancies.json"))