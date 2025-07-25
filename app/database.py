from sqlmodel import SQLModel, create_engine, Session


DATABASE_URL = "sqlite:///./geoapp.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)