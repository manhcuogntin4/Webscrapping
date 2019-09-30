from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'golds',
    user='golds',
    password='golds',
    host='localhost',
    port=5432,
    autorollback=True
)