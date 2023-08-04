from config import config
from src.utils import get_employers, create_database, filling_database_hh_data, create_table_in_bd
from src.postgres_db import DBManager


def main():
    companies_id = [78638,  # Тинькофф
                    8884,  # dr.Web
                    2324020,  # Финтех
                    5179890,  # Enjoypro
                    67611,  # Tensor
                    1795976,  # ITMO
                    3202190,  # KTS
                    1993194,  # Yadro
                    3292313,  # Holyweb
                    4649269,  # Иннотех
                    ]

    database_name = 'hh_employer'

    params = config()

    data = get_employers(companies_id)
    create_database(database_name, params)
    create_table_in_bd(database_name, params)
    filling_database_hh_data(data, database_name, params)

    db_manager = DBManager(database_name)


if __name__ == "__main__":
    main()
