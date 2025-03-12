from fastapi import FastAPI
from app.core.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API is running!"}

@app.get("/home")
def read_root():
    return {"message": "Welcome to home page baby!"}