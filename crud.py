from sqlalchemy.orm import Session
import models
import schemas

# Gets all the todo items from the database
def get_all_todos(db:Session):
    return db.query(models.Todo).all()

# Gets a single todo item by ID.
def get_todo(db:Session, todo_id : int):
    return db.query(models.Todo).filter(models.Todo.id==todo_id).first()

# Adds a new todo to the database.
def create_todo(db:Session, todo : schemas.TodoCreate):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db:Session, todo_id : int, todo : schemas.TodoCreate ):
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.completed = todo.completed
        db.commit()
        db.refresh(db_todo)
    return db_todo


def delete_todo(db:Session, todo_id : int):
    todo = get_todo(db, todo_id)
    if todo:
        db.delete(todo)
        db.commit()
    return todo