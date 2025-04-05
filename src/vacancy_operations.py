from src.utils import read_json_file
from src.utils import clean_search_teg

class Vacancy:
    """Класс представления вакансии"""

    def __init__(
        self,
        vacancy_id,
        name,
        area,
        salary,
        url,
        snippet_requirement,
        snippet_responsibility,
    ):
        self.vacancy_id = vacancy_id
        self.name = name
        self.area = area
        self.salary = salary
        self.url = url
        self.snippet_requirement = snippet_requirement
        self.snippet_responsibility = snippet_responsibility


    def __repr__(self):
        return (f"[{self.vacancy_id}, {self.name}, {self.area}, {self.salary}, {self.url}, {self.snippet_requirement},"
                f"{self.snippet_responsibility}]")


    @property
    def salary_from(self):
        return self.salary.get("from", 0)
    #
    @property
    def salary_to(self):
        return self.salary.get("to", 0)

class VacanciesList():
    """ Класс для работы со списком вакансий """

    vacancies: list

    def __init__(self, vacancies=None):
        self.__vacancies = vacancies if vacancies else []

    def __repr__(self):
        return f"{self.__vacancies}"



    @classmethod
    def converted_to_class(cls, file_path):
        """Преобразование JSON файла в объект класса"""
        vacancies = []
        data = read_json_file(file_path)
        for item in data.get("items", []):
            vacancy = Vacancy(
                vacancy_id = item.get("id"),
                name = item.get("name", ""),
                area = item.get("area", {}).get("name", ""),
                salary = item.get("salary", {}),
                url = item.get("alternate_url", ""),
                snippet_requirement = clean_search_teg(item.get("snippet", "").get("requirement")),
                snippet_responsibility = clean_search_teg(item.get("snippet", "").get("requirement")),
            )
            print(item.get("salary"))
            vacancies.append(vacancy)
        return cls(vacancies)






if __name__ == "__main__":

    res = VacanciesList.converted_to_class("vacancies.json")

    print("До сортировки")
    print(res)

    res.sort_by_salary(False)
    print("После сортировки")
    print(res)


