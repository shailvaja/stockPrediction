import psycopg2
import config
import csv
def open_connection():
    conn = None
    try:
        # read connection parameters
        params = config.config()
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.close()


def close_connection( conn):
    if conn is not None:
        conn.close()


def load_csv_table(file_name, table):
    conn = open_connection()
    cur = conn.cursor()
    prev_count = "Select count("
    query = "INSERT INTO " + table + " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute(
                query,
                row
            )
    conn.commit()
    close_connection(conn)


