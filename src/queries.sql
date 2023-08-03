--1 получает список всех компаний и количество вакансий у каждой компании.

SELECT title_employer,count(vacancies.title_vacancy) FROM employer
JOIN vacancies USING(employer_id)
GROUP BY title_employer

--2 получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию


--3 получает среднюю зарплату по вакансиям.

SELECT round(AVG(salary)) FROM vacancies

--4 получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.

SELECT * from vacancies
WHERE salary > (SELECT round(AVG(salary)) from vacancies)

--5 получает список всех вакансий, в названии которых содержатся переданные в метод слова

SELECT * FROM vacancies WHERE title_vacancy LIKE '%Python%'