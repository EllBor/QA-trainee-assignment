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
    return valid_item["sellerID"]

# Позитивные тесты

def test_get_items_by_valid_seller(created_item):
    response = requests.get(f"{BASE_URL}/{created_item}/item")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(item["sellerId"] == created_item for item in response.json())

# Негативные тесты

def test_get_items_by_seller_invalid_format():
    response = requests.get(f"{BASE_URL}/invalid_seller_id/item")
    assert response.status_code == 400

def test_get_items_by_empty_seller():
    response = requests.get(f"{BASE_URL}//item")
    assert response.status_code == 405
