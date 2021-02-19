import psycopg2
import os 

# Get environment variables
USER = os.getenv('')
PASSWORD = os.environ.get('')
HOST = os.environ.get('')
PORT = os.environ.get('')
DATABASE = os.environ.get('')

if USER is None:
    USER = "postgres"
if PASSWORD is None:
    PASSWORD = "password"
if HOST is None:
    HOST = "host"
if DATABASE is None:
    DATABASE = "postgres"         
if PORT is None:
    PORT = "5432"
conn = None 
try : 
    conn = psycopg2.connect(
        host= HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,port = PORT)
    print(dir(conn))
    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
    cur.close()
    

except psycopg2.Error as e:
    print("Error code:", e.pgcode,"\nError:",e.pgerror )

finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
        




