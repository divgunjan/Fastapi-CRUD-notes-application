'''
the notes app has one data which is a Note object with different attributes;
id:int, title:string, noteBody:string
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes" #the table of db to store under "notes" with __tablename__ attribute 
    id = Column(Integer, primary_key=True) #id value of type int, specified as primary_key(cannot have null value) 
    title = Column(String) #title of the notes
    noteBody = Column(String) #note-taking area
    
#repr functions are designed to provide readable string outputs instead of unreadable compiler messages 
def __repr__(self):
    return f"Note(id={self.id}, title={self.title}, noteBody ={self.noteBody})"
