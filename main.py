from fastapi import FastAPI
import uvicorn
from routes.users import user_router
from routes.events import event_router
from database.connection import Settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

settings = Settings()

# Register routes
app.include_router(user_router, prefix='/user')
app.include_router(event_router, prefix='/event')

# allow requests from any origin on the world wide web
origins = ['*']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Initialize the database when the app starts
@app.on_event('startup')
async def init_db():
    await settings.initialize_database()

# Run server
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
