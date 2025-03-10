from fastapi.testclient import TestClient
from main import app

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3,
        "sepal_width": 5,
        "petal_length": 3.2,
        "petal_width": 4.4,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Virginica"}


# test to check if Iris Setosa is classified correctly
def test_pred_Setosa():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 4.9,
        "sepal_width": 3.0,
        "petal_length": 1.4,
        "petal_width": 0.1,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json()["flower_class"] == "Iris Setosa"

# test to check if Iris Versicolour is classified correctly
def test_pred_Versicolour():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 5.8,
        "sepal_width": 2.6,
        "petal_length": 4.1,
        "petal_width": 1.0,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json()["flower_class"] == "Iris Versicolour"

# test to check the correct functioning of the /feedback_loop route
def test_feedback_loop():
    payload = [{
        "sepal_length": 3.0,
        "sepal_width": 5.0,
        "petal_length": 3.2,
        "petal_width": 4.4,
        "flower_class": "Iris Virginica"
    }]
    with TestClient(app) as client:
        response = client.post("/feedback_loop", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"detail": "Feedback loop successful"} 