
from fastapi import FastAPI
from pydantic import BaseModel
from app.matcher import find_best_match
import json

app = FastAPI()

with open("data/students.json") as f:
    student_pool = json.load(f)

with open("config.json") as f:
    config = json.load(f)

class MatchRequest(BaseModel):
    student_id: str
    goal: str
    preferred_study_time: str
    study_type: str
    personality: list

@app.post("/match")
def match_student(request: MatchRequest):
    result = find_best_match(request.dict(), student_pool, config)
    return result

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/version")
def version_info():
    return {"version": config.get("version", "unknown")}
