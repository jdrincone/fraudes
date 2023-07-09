import pandas as pd
import psycopg2
import yaml

from fraudes.python.metadata.paths import Paths


def read_table_from_bd(name_table: str = "fraudes") -> pd.DataFrame:
    """Lee tabla desde base de datos.
    Arg:
        name_table: nombre de tabla a leer.

    Return:
        DataFrame solicitado.
    """
    with open(Paths.cred_posgres) as file:
        cred = yaml.full_load(file)

    try:
        connection = psycopg2.connect(
            host=cred["host"],
            user=cred["user"],
            password=cred["password"],
            database=cred["database"],
        )

        with open(Paths.query) as file:
            querys = yaml.full_load(file)

        query = querys[name_table]
        cur = connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        columns = [i[0] for i in cur.description]
        df = pd.DataFrame(data, columns=columns)

    except Exception as e:
        print(e)
        print(f"Se generó un error consultando la tabla: {name_table}")
        raise Exception

    return df


if __name__ == "__main__":
    table = read_table_from_bd()
    print(table)
