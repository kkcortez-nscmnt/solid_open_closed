from repositorio import Respositorio
from databases import PostgresDB

db_con = PostgresDB()
repo = Respositorio()

repo.insert(db_con)