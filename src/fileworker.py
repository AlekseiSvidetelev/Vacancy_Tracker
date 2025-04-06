from abc import ABC, abstractmethod


class Saver(ABC):

    def __init__(self,file_name):

        self.__file_name = file_name if file_name else "vacancies.json"

    @property
    def file_name(self):
        return self.__file_name


    @abstractmethod
    def read_to_file(self):
        pass


    @abstractmethod
    def save_to_file(self):
        pass


class JSONSaver:

    def __init__(self, file_name):
        super().__init__(file_name)
        self.__file_name = file_name if file_name else "vacancies.json"



    def save_json_file(filename_json: str, vacancies: dict[str, Any]) -> None:
        """Функция для записи данных в JSON файла"""
        try:
            with open(os.path.join(DATA_DIR, filename_json), "w", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    def read_json_file(filename_json: str) -> dict[str, Any]:
        """Функция для чтения JSON файла в список"""
        try:
            with open(os.path.join(DATA_DIR, filename_json), "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"Ошибка при чтении файла {Exception}: {e} ")
            return {}