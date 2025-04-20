from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_create_and_mark_done():
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 200
    task = response.json()
    assert task["title"] == "Test task"
    assert task["is_done"] is False

    task_id = task["id"]
    response = client.patch(f"/tasks/{task_id}/done")
    assert response.status_code == 200
    updated = response.json()
    assert updated["is_done"] is True
