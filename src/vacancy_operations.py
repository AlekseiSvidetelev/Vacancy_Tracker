from src.utils import read_json_file


class Vacancies:
    """Класс для работы с вакансиями"""

    def __init__(
        self,
        name,
        area,
        salary,
        url,
        snippet_requirement,
        snippet_responsibility,
        schedule,
        work_format,
        working_hours,
        professional_roles,
        work_schedule_by_days,
        employment_form,
    ):
        self.name = name
        self.area = area
        self.salary = salary
        self.url = url
        self.snippet_requirement = snippet_requirement
        self.snippet_responsibility = snippet_responsibility
        self.schedule = schedule
        self.work_format = work_format
        self.working_hours = working_hours
        self.professional_roles = professional_roles
        self.work_schedule_by_days = work_schedule_by_days
        self.employment_form = employment_form

    @classmethod
    def converted_to_class(cls, file_path):
        """Преобразование JSON файла в объект класса"""
        vacancies = []
        data = read_json_file(file_path)
        for item in data.get("items", []):
            name = item.get("name", "")
            area = item.get("area", {}).get("name", "")
            salary = item.get("salary", {})
            url = item.get("alternate_url", "")
            snippet_requirement = item.get("snippet", "").get("requirement")
            snippet_responsibility = item.get("snippet", "").get("requirement")
            schedule = item.get("schedule", {}).get("name", "")
            work_format = item.get("work_format", [])
            working_hours = item.get("working_hours", [])
            professional_roles = item.get("professional_roles", [])
            work_schedule_by_days = item.get("work_schedule_by_days", [])
            employment_form = item.get("employment_form", {})

            vacancy = cls(
                name,
                area,
                salary,
                url,
                snippet_requirement,
                snippet_responsibility,
                schedule,
                work_format,
                working_hours,
                professional_roles,
                work_schedule_by_days,
                employment_form,
            )
            vacancies.append(vacancy)

        return vacancies




if __name__ == "__main__":
    res = repr(Vacancies.converted_to_class("vacancies.json"))
    print(res)
