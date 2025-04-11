from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
        
# API Routes

@app.post('/todos/', response_model=schemas.TodoOut)
def create(todo : schemas.TodoCreate, db : Session = Depends(get_db)):
    return crud.create_todo(db , todo)


@app.get('/todos/', response_model=list[schemas.TodoOut])
def read_all(db : Session = Depends(get_db)):
    return crud.get_all_todos(db)


@app.get('/todos/{todo_id}', response_model=schemas.TodoOut)
def read_one(todo_id : int, db : Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put('/todos/{todo_id}', response_model=schemas.TodoOut)
def update(todo_id : int, todo : schemas.TodoCreate ,db : Session = Depends(get_db)):
    updated = crud.update_todo(todo_id, db, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


@app.delete('/todos/{todo_id}')
def delete(todo_id : int, db : Session = Depends(get_db)):
    deleted = crud.delete_todo(todo_id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail= "Todo not found")
    return deleted