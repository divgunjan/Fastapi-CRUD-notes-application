from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "sqlite:///./db.sql" 

'''
url points to the db.sql file; automatically created by sqlalchemy
the db reference is used by sessionmaker to create a db session 
'instance(DBSession), used to connect and interact with the db later on
'''

engine = create_engine(SQLALCHEMY_DB_URL, echo=True)
DBSession = sessionmaker(engine, autoflush=False)




