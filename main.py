from fastapi import FastAPI
import uvicorn
from routes.users import user_router
from routes.events import event_router
from database.connection import conn


app = FastAPI()

# Register routes
app.include_router(user_router, prefix='/user')
app.include_router(event_router, prefix='/event')

# Creating a database when the app starts
@app.on_event("startup")
def on_startup():
    conn()


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
