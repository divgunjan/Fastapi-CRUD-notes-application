'''
1. to ensure that there's always a table in the db corresponding to our defined models.
For this, we define the __init__.py file for the model package to work.
'''

from . import model, database
model.Base.metadata.create_all(bind = database.engine)

'''
2. everytime one imports the models package or something from it, 
this(models.Base.metadata.create_all(bind=database.engine)) checks if the defined models have corresponding tables in the db else sqlalchemy will create them.
'''


