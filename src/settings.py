import os

from loadotenv import load_env

load_env()

DB_URI = os.getenv('DB_URI')


def get_indexes(table):
    """
    Return all columns and indexes for a given table
    :param table: (sqlalchemy.sql.schema.Table) table object
    :return: list of columns and keys
    """
    columns = [c.name for c in table.columns]

    keys = list()
    for i in table.indexes:
        for c in i.columns:
            keys.append(c.name)

    return columns, keys
