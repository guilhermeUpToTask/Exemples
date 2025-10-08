import uuid
import pytest
from tests.utils import create_product_via_api


def test_get_product(client):
    payload = {
        "name": "Blue Jeans",
        "category": "jeans",
        "price": 99.99,
        "description": "A Blue Jeans",
    }

    created_product = create_product_via_api(client, **payload)
    get_response = client.get(f"/products/{created_product['id']}")
    assert get_response.status_code == 200

    retrieved_product = get_response.json()
    assert "id" in retrieved_product
    assert retrieved_product["name"] == payload["name"]
    assert retrieved_product["category"] == payload["category"]
    assert float(retrieved_product["price"]) == pytest.approx(payload["price"])
    assert retrieved_product["description"] == payload["description"]


def test_get_product_wrong_type(client):
    get_response = client.get(f"/products/wrong-id-type")
    assert get_response.status_code == 422

    body = get_response.json()
    assert body["detail"][0]["type"] == "uuid_parsing"


def test_get_product_not_found(client):
    fake_id = uuid.uuid4()
    assert client.get(f"/products/{fake_id}").status_code == 404
