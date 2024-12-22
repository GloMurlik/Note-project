from pydantic import BaseModel
from datetime import datetime

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):  # Наследуем NoteBase
    pass

class NoteUpdate(NoteBase):  # Наследуем NoteBase
    pass

class NoteInDB(NoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Note(NoteInDB):  # Наследуем NoteInDB
    pass

