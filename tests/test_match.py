
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_match_success():
    response = client.post("/match", json={
        "student_id": "stu_1000",
        "goal": "Crack GATE 2025",
        "preferred_study_time": "early_morning",
        "study_type": "visual",
        "personality": ["focused", "introvert"]
    })
    assert response.status_code == 200
    assert "matched_student_id" in response.json()
