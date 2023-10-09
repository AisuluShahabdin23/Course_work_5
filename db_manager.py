import psycopg2


class DBManager:
    def __init__(self, database, params):
        self.dbname = database
        self.params = params
        self.conn = psycopg2.connect(dbname=database, **params)

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании
        """
        query = """
                SELECT employer, COUNT(*) AS vacancies_count
                FROM vacancies
                GROUP BY employer;
                """
        with self.conn.cursor() as cur:
            cur.execute(query)
            results = cur.fetchall()
            # return results
            for company, vacancies_count in results:
                print(f"компания: {company}, количество вакансий: {vacancies_count}")

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию
        """
        query = """
                SELECT * FROM vacancies
                """
        with self.conn.cursor() as cur:
            cur.execute(query)
            results = cur.fetchall()
            # return results
            for name, employer, salary, id, url in results:
                print(f"компания: {employer}, вакансия: {name}, зарплата: {salary}, ссылка: {url}")

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        """
        query = """
                SELECT AVG(salary) AS avg_salary
                FROM vacancies 
                WHERE salary IS NOT NULL;
                """
        with self.conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchone()
            # return results
            print(f" Средняя зарплата: {round(result[0])}")

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        query = """
                SELECT * 
                FROM vacancies 
                WHERE salary > (SELECT AVG(salary) FROM vacancies)
                ORDER BY salary DESC;
                """
        with self.conn.cursor() as cur:
            cur.execute(query)
            results = cur.fetchall()
            # return results
            for name, employer, salary, id, url in results:
                print(f"компания: {employer}, вакансия: {name}, зарплата: {salary}, ссылка: {url}")

    def get_vacancies_with_keyword(self, query):
        """
        Получает список всех вакансий, в названии которых содержатся
        переданные в метод слова, например “python”
        """
        query = """
                SELECT name 
                FROM vacancies
                WHERE name LIKE '%{word}%'
                ORDER BY name;
                """
        with self.conn.cursor() as cur:
            cur.execute(query)
            results = cur.fetchall()
            # return results
            for name, employer, id, salary, url in results:
                print(f"компания: {employer}, вакансия: {name}, зарплата: {salary}, ссылка: {url}")
