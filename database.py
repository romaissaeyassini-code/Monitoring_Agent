import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
from sqlalchemy.orm import declarative_base , sessionmaker


DATABASE_URL= "postgresql+psycopg://roro:0000@192.168.40.129:5432/fastapi_database"

engine = sql.create_engine(DATABASE_URL)


sessionlocal= sessionmaker(
    autocommit= False,
    autoflush= False , 
    bind=engine)

base=declarative_base()