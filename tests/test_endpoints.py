from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "name": "John",
        "age": 25,
        "gender": "male",
        "email": "john@example.com",
        "city": "New York",
        "interests": "movies,reading"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "john@example.com"

# Add tests for update, delete, and match endpoints.
