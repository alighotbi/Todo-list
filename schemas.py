from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False
    
class TodoOut(TodoCreate):
    id: int
    
    class Config:
        orm_mode = True