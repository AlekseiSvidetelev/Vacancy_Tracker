class Vacancies:

    def __init__(self, title, url, salary, company, description, experience=None, schedule=None):

        self.title = title
        self.url = url
        self.salary = salary
        self.company = company
        self.description = description
        self.experience = experience
        self.schedule = schedule

    def get_salary(self, salary_data):
        pass

    @classmethod
    def cast_to_object_list(
        cls,
    ):
        """Преобразование данных из JSON файла в список объектов Vacancies"""
        vacancies = []
