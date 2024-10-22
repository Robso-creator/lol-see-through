from sqlalchemy import create_engine
from sqlalchemy import inspect

from src import settings


def send_to_db(df, table_name):
    print('RUNNING SAVE ON DB | ', table_name)
    engine = create_engine(settings.DB_URI)

    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        raise ValueError(f"Tabela '{table_name}' não existe no banco de dados")

    print('GETTING TABLE COLS | ', table_name)
    existing_columns = inspector.get_columns(table_name)
    existing_column_names = [col['name'] for col in existing_columns]

    print('REINDEXING DATAFRAME | ', table_name)
    df.reindex(columns=[existing_column_names])
    df = df[existing_column_names]

    print('SENDING TO DB | ', table_name)
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',
        index=False,
    )
    print('DONE | ', table_name)
