import psycopg2
class DBManager():
    def get_companies_and_vacancies_count():
        '''получает список всех компаний и количество вакансий у каждой компании.'''
        pass
    def get_all_vacancies():
        '''получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию'''
        pass

    def get_avg_salary():
        '''получает среднюю зарплату по вакансиям.'''
        pass

    def get_vacancies_with_higher_salary():
        '''получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.'''
        pass
    def get_vacancies_with_keyword():
        '''получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.'''
        pass
    def get_data_from_API(self):
        '''Метод получения данных по API'''
        v_hh = []
        URL = 'https://api.hh.ru/employers'
        for page in range(1, 11):
            params = {
                'per_page': 100,
                'area': 113,
                'page': page,
                'text': self.user_request,
                'only_with_salary': True
            }
            response = requests.get(URL, params=params).json()
            v_hh.extend(response['items'])
        return v_hh