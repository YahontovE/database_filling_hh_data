import requests
import psycopg2


def get_employers(companies_id):
    """
    В качестве аргумента принимает список с id компаниями
    Возвращает список словарей формата
    {company:
    vacancies: }
    """
    employers = []
    for company in companies_id:
        url = f'https://api.hh.ru/employers/{company}'
        company_response = requests.get(url).json()
        vacancy_response = requests.get(company_response['vacancies_url']).json()
        employers.append({
            'company': company_response,
            'vacancies': vacancy_response['items']
        })

    return employers


def create_database(database_name, params):
    '''Создаем базу данных и таблиц'''
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f'DROP DATABASE {database_name}')
    except:
        cur.execute(f'CREATE DATABASE {database_name}')
    else:
        cur.execute(f'CREATE DATABASE {database_name}')
    finally:
        cur.close()
        conn.close()


def create_table_in_bd(database_name, params):
    '''Создаем таблицы в базе данных hh_employer'''
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE employer (
                    employer_id SERIAL PRIMARY KEY,
                    title_employer VARCHAR(255) NOT NULL,
                    city VARCHAR(255),
                    field_of_activity TEXT,
                    site_url TEXT
                )
            """)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE vacancies (
                    vacancy_id SERIAL PRIMARY KEY,
                    employer_id INT REFERENCES employer (employer_id) NOT NULL,
                    title_vacancy VARCHAR(255) NOT NULL,
                    publish_date DATE,
                    vacancy_url TEXT
                )
            """)

    conn.commit()
    conn.close()


def filling_database_hh_data(database_data, database_name, params):
    '''Заполение таблиц данными полученымы с hh.ru'''
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        for company in database_data:
            company_data = company['company']
            cur.execute(
                """
                INSERT INTO employer (title_employer,city,field_of_activity,site_url)
                VALUES (%s, %s, %s, %s)
                RETURNING employer_id
                """,
                (company_data['name'], company_data['area']['name'], company_data['industries'][1]['name'],
                 company_data['site_url'])
            )
            employer_id = cur.fetchone()[0]
            vacancies_data = company['vacancies']
            for inf in vacancies_data:
                # vacancy_data=inf['vacancies']
                cur.execute(
                    """
                    INSERT INTO vacancies (employer_id, title_vacancy, publish_date,vacancy_url)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (employer_id, inf['name'], inf['published_at'][:10], inf['alternate_url'])
                )

    conn.commit()
    conn.close()

# companies=[78638,8884]
# print(get_employers(companies))
