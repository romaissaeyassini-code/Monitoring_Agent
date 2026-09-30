import database
import models

def create_tables():
    database.base.metadata.create_all(bind=database.engine)
