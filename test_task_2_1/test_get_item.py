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

def test_get_item_by_valid_id(created_item):
    response = requests.get(f"{BASE_URL}/item/{created_item}")
    assert response.status_code == 200
    data = response.json()[0]
    assert data["id"] == created_item
    assert "sellerId" in data
    assert "name" in data
    assert "price" in data
    assert "statistics" in data
    assert isinstance(data["statistics"]["likes"], int)
    assert isinstance(data["statistics"]["viewCount"], int)
    assert isinstance(data["statistics"]["contacts"], int)

# Негативные тесты

def test_get_nonexistent_item():
    response = requests.get(f"{BASE_URL}/item/invalid_id")
    assert response.status_code == 400

def test_get_item_invalid_format():
    response = requests.get(f"{BASE_URL}/item/!@#$%^&*()")
    assert response.status_code == 400

def test_get_item_empty_id():
    response = requests.get(f"{BASE_URL}/item/")
    assert response.status_code == 404

def test_get_item_null_id():
    response = requests.get(f"{BASE_URL}/item/null")
    assert response.status_code == 400

def test_get_item_too_long_id():
    long_id = "a" * 1000
    response = requests.get(f"{BASE_URL}/item/{long_id}")
    assert response.status_code == 400
