from sqlalchemy import column, Integer, String, Boolean
from database import Base

class Todo(Base):
    __tablename__ = "todos"
    
    id = column(Integer, primary_key = True, index=True)
    title = column(String, index=True)
    description = column(String, nullable=True)
    completed = column(Boolean, default=False)