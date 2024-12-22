from fastapi import FastAPI
from app.routers import notes
from app.database import engine
from app.models import Base
from app import database, routers

# Создаем приложение FastAPI
app = FastAPI(title="Notes Service", description="Сервис для управления заметками")

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

database.init_db()
# Подключение роутов
app.include_router(notes.router, prefix="/notes", tags=["Notes"])



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

