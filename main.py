import os
from config import config
from utils import *
from create_db import create_db, fill_table_companies, fill_table_vacancies
from db_manager import DBManager


def main():
    params = config()

    create_db('hh', params)
    employers = get_employers_data()
    vacancies = get_vacancies_data()

    fill_table_companies(employers, 'hh', params)
    fill_table_vacancies(vacancies, 'hh', params)

    db_manager = DBManager('hh', params)

    db_manager.get_companies_and_vacancies_count()
    db_manager.get_avg_salary()
    db_manager.get_all_vacancies()
    db_manager.get_vacancies_with_higher_salary()
    db_manager.get_vacancies_with_keyword("python")


if __name__ == '__main__':
    main()
