from pydantic import BaseModel, EmailStr

class TodoCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False
    
class TodoOut(TodoCreate):
    id: int
    
    class Config:
        orm_mode = True

        
class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password : str
    

class UserResponse(BaseModel):
    id : int
    username : str
    email : EmailStr 
    
    class Config:
        orm_mode = True