import psycopg2
from config import config


class DBManager:

    def __init__(self, database_name='hh_employer', params=config()):
        self.database_name = database_name
        self.params = params
        #self.conn = psycopg2.connect(dbname=self.database_name, **self.params)

    def get_companies_and_vacancies_count(self):
        '''получает список всех компаний и количество вакансий у каждой компании.'''
        conn = psycopg2.connect(dbname=self.database_name,**self.params)
        with conn.cursor() as cur:
            cur.execute("SELECT title_employer,count(vacancies.title_vacancy) "
                        "FROM employer JOIN vacancies USING(employer_id) "
                        "GROUP BY title_employer")
            rows = cur.fetchall()
        conn.close()
        return rows

    def get_all_vacancies(self):
        '''получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию'''
        pass

    def get_avg_salary(self):
        '''получает среднюю зарплату по вакансиям.'''
        pass

    def get_vacancies_with_higher_salary(self):
        '''получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.'''
        pass

    def get_vacancies_with_keyword(self):
        '''получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.'''
        pass


#q=DBManager('hh_employer',parm)
#print(q.get_companies_and_vacancies_count())