from sqlmodel import SQLModel, Session, create_engine
from models.events import Event


database_file = "plannder.db"
database_connection_string = f'sqlite:///{database_file}'
connect_args = {'check_same_thread': False}
engine_url = create_engine(database_connection_string, 
                           echo=True, 
                           connect_args=connect_args)


def conn():
    """
        Creates a database.
    """
    SQLModel.metadata.create_all(engine_url)

def get_session():
    """
        Persists the session in the app.
    """
    with Session(engine_url) as session:
        yield session
