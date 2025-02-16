import requests
import pytest

BASE_URL = "https://qa-internship.avito.com/api/1"

@pytest.fixture
def valid_item():
    return {
        "sellerID": 123456,
        "name": "Test Item",
        "price": 1000,
        "statistics": {
            "contacts": 3,
            "likes": 10,
            "viewCount": 50
        }
    }

@pytest.fixture
def created_item(valid_item):
    response = requests.post(f"{BASE_URL}/item", json=valid_item)
    assert response.status_code == 200
    data = response.json()
    status = data.get("status")
    item_id = status.split(" - ")[1]
    return item_id

# Позитивные тесты

def test_get_item_statistics(created_item):
    response = requests.get(f"{BASE_URL}/statistic/{created_item}")
    assert response.status_code == 200
    data = response.json()[0]
    assert "likes" in data
    assert "viewCount" in data
    assert "contacts" in data
    assert isinstance(data["likes"], int)
    assert isinstance(data["viewCount"], int)
    assert isinstance(data["contacts"], int)

# Негативные тесты

def test_get_statistics_nonexistent():
    response = requests.get(f"{BASE_URL}/statistic/invalid_id")
    assert response.status_code == 400

def test_get_statistics_invalid_format():
    response = requests.get(f"{BASE_URL}/statistic/!@#$%^&*()")
    assert response.status_code == 400

def test_get_statistics_empty_id():
    response = requests.get(f"{BASE_URL}/statistic/")
    assert response.status_code == 404

def test_get_statistics_null_id():
    response = requests.get(f"{BASE_URL}/statistic/null")
    assert response.status_code == 400