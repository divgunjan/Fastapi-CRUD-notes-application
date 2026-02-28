#building the api
from fastapi import FastAPI, HTTPException
from schemas import NoteInput
from model.database import DBSession
from model import models
from sqlalchemy.orm.exc import UnmappedInstanceError

from fastapi.middleware.cors import CORSMiddleware

#app instance creation
app = FastAPI()

'''defining the api routes
1.Create
2.Read
3.Update
4.Delete
'''

#accessing a note for reading
@app.get('/notes')
def read_notes():    
    db = DBSession()#database instance to query all the entries
    try:
        notes=db.query(models.Note).all()
    finally:
        db.close() #db should close regardless of request succeeding/not
    return notes #returns notes as the HTTP GET response of the API route  

#creating a new note
@app.post('/note')
def add_note(note:NoteInput):
    db = DBSession()
    try:
        if len(note.title) == 0 and len(note.noteBody) == 0:
            raise HTTPException(
                status_code=400,
                detail={
                    "status":"Error 400 - Bad Request",
                    "message":"Both 'title' and 'noteBody' are empty" 
                })
        new_note = models.Note(title = note.title, note_body=note.noteBody)
        db.add(new_note)
        db.commit()
        db.refresh(new_note)

    finally:
        db.close()
    return new_note

#updating a note
'''
takes 2 database operations,
1.query the note through its id,
2.update the resulting note query's data, -> updated_note

this note will require client to pass id
'''

@app.put("/note/{note_id}")
def update_note(note_id:int,updated_note:NoteInput):
    db = DBSession()
    if len(updated_note.title) == 0 and len(updated_note.noteBody) == 0:
        raise HTTPException(
            status_code=400,
            detail={
                "status":"Error 400 - Bad Request",
                "message":"The note's 'title' and 'noteBody' can't be both empty"
            })
    try:
        note_obj = db.query(models.Note).filter(models.Note.id == note_id).first()
        if not note_obj:
            raise HTTPException(status_code=404, detail={
                "status": "Error 404 - Not Found",
                "message": f"Note with id '{note_id}' does not exist."
            })
        note_obj.title = updated_note.title
        note_obj.note_body = updated_note.noteBody
        db.commit()
        db.refresh(note_obj)
    finally:
        db.close()
    return note_obj        

#deleting a note
@app.delete("/note/{note_id}")
def delete_note(note_id:int):
    db=DBSession()
    try:
        note_obj = db.query(models.Note).filter(models.Note.id == note_id).first()
        if not note_obj:
            raise HTTPException(status_code=404, detail={
                "status": "Error 404 - Not Found",
                "message": f"Note with id '{note_id}' does not exist."
            })
        db.delete(note_obj)
        db.commit()
    except UnmappedInstanceError:
        raise HTTPException(status_code=400, detail={ 
            "status": "Error 400 - Bad Request", 
            "message" : f"Note with id '{note_id}' could not be deleted."
        })

    finally:
        db.close()
 
    return{
        "status":"200",
        "message":"Note deleted successfully"
    }

#CORS
origins = ["http://localhost:3000"]

#defining the middleware and the methods related to it
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods = ["*"], # '*' = allow all 
    allow_headers = ["*"]
)

