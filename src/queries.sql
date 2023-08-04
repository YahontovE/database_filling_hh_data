--1 получает список всех компаний и количество вакансий у каждой компании.

SELECT title_employer,count(vacancies.title_vacancy) FROM employer
JOIN vacancies USING(employer_id)
GROUP BY title_employer

--2 получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию

SELECT employer.title_employer,vacancies.title_vacancy,
vacancies.salary_from,vacancies.vacancy_url FROM vacancies
JOIN employer USING(employer_id)

--3 получает среднюю зарплату по вакансиям.

SELECT round(AVG(salary_from)) FROM vacancies

--4 получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.

SELECT title_vacancy from vacancies
WHERE salary_from > (SELECT round(AVG(salary_from)) from vacancies)

--5 получает список всех вакансий, в названии которых содержатся переданные в метод слова

SELECT title_vacancy FROM vacancies WHERE title_vacancy LIKE '%Python%'