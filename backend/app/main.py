from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Backend is running successfully",
        "project_id": os.getenv("PROJECT_ID")
    }