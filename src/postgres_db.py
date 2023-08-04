import psycopg2


class DBManager:

    def __init__(self, database_name='hh_employer'):
        self.database_name = database_name
        self.conn = psycopg2.connect(host='localhost', database=self.database_name,
                                     user='postgres', password='Vidineeva')

    def get_companies_and_vacancies_count(self):
        '''получает список всех компаний и количество вакансий у каждой компании.'''
        with self.conn.cursor() as cur:
            cur.execute("SELECT title_employer,count(vacancies.title_vacancy) "
                        "FROM employer JOIN vacancies USING(employer_id) "
                        "GROUP BY title_employer")
            rows = cur.fetchall()
        self.conn.close()
        return rows

    def get_all_vacancies(self):
        '''получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию'''
        with self.conn.cursor() as cur:
            cur.execute("SELECT employer.title_employer,vacancies.title_vacancy,"
                        "vacancies.salary_from,vacancies.vacancy_url"
                        " FROM vacancies JOIN employer USING(employer_id)")
            rows = cur.fetchall()
        self.conn.close()
        return rows

    def get_avg_salary(self):
        '''получает среднюю зарплату по вакансиям.'''
        with self.conn.cursor() as cur:
            cur.execute("SELECT round(AVG(salary_from)) FROM vacancies")
            rows = cur.fetchall()
        self.conn.close()
        return rows

    def get_vacancies_with_higher_salary(self):
        '''получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.'''
        with self.conn.cursor() as cur:
            cur.execute("SELECT * from vacancies "
                        "WHERE salary_from > (SELECT round(AVG(salary_from)) FROM vacancies)")
            rows = cur.fetchall()
        self.conn.close()
        return rows

    def get_vacancies_with_keyword(self):
        '''получает список всех вакансий,
         в названии которых содержатся переданные в метод слова, например “python”.'''
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM vacancies WHERE title_vacancy LIKE '%Python%'")
            rows = cur.fetchall()
        self.conn.close()
        return rows