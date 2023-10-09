Получает список всех компаний и количество вакансий у каждой компании
query = SELECT employer, COUNT(*) AS vacancies_count
        FROM vacancies
        GROUP BY employer

Получает список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию
query = SELECT * from vacancies

Получает среднюю зарплату по вакансиям
query = SELECT AVG(salary) AS avg_salary
        FROM vacancies
        WHERE salary IS NOT NULL

Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
query = SELECT * FROM vacancies
        WHERE salary > (SELECT AVG(salary) FROM vacancies)
        ORDER BY salary DESC

Получает список всех вакансий, в названии которых содержатся переданные в метод слова
query = SELECT name
        FROM vacancies
        WHERE name LIKE '%{word}%'
        ORDER BY name