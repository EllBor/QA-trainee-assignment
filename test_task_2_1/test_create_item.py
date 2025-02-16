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

# Позитивные тесты

def test_create_item(valid_item):
    response = requests.post(f"{BASE_URL}/item", json=valid_item)
    assert response.status_code == 200
    data = response.json()
    assert "status" in data or "Сохранили" in data["status"]

def test_create_item_minimal_required_fields():
    minimal_item = {
        "sellerID": 654321,
        "name": "Minimal Item",
        "price": 1
    }
    response = requests.post(f"{BASE_URL}/item", json=minimal_item)
    assert response.status_code == 200
    assert "status" in response.json()

# Негативные тесты

def test_create_item_missing_fields():
    invalid_item = {
        "name": "Test Item",
        "price": 1000
    }
    response = requests.post(f"{BASE_URL}/item", json=invalid_item)
    assert response.status_code == 400

def test_create_item_invalid_price(valid_item):
    valid_item["price"] = -100
    response = requests.post(f"{BASE_URL}/item", json=valid_item)
    assert response.status_code == 400

def test_create_item_empty_name(valid_item):
    valid_item["name"] = ""
    response = requests.post(f"{BASE_URL}/item", json=valid_item)
    assert response.status_code == 400

def test_create_item_large_price(valid_item):
    valid_item["price"] = 10**10
    response = requests.post(f"{BASE_URL}/item", json=valid_item)
    assert response.status_code == 400

def test_create_item_null_values():
    invalid_item = {
        "sellerID": None,
        "name": None,
        "price": None
    }
    response = requests.post(f"{BASE_URL}/item", json=invalid_item)
    assert response.status_code == 400
