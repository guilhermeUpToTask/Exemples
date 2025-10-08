import uuid
import pytest
from tests.utils import create_product_via_api


def test_update_product_success(client):
    create_payload = {
        "name": "Blue Jeans",
        "category": "jeans",
        "price": 99.99,
        "description": "A Blue Jeans",
    }
    created_product = create_product_via_api(client, **create_payload)

    update_payload = {
        "name": "Yellow T-Shirt",
        "category": "t-shirts",
        "price": 199.99,
        "description": "A Yellow T-Shirt",
    }
    patch_response = client.patch(
        f"/products/{created_product['id']}", json=update_payload
    )
    assert patch_response.status_code == 200

    updated_product = patch_response.json()
    assert updated_product["id"] == created_product["id"]
    assert updated_product["name"] == update_payload["name"]
    assert updated_product["category"] == update_payload["category"]
    assert float(updated_product["price"]) == pytest.approx(update_payload["price"])
    assert updated_product["description"] == update_payload["description"]


def test_patch_update_product(client):
    create_payload = {
        "name": "Blue Jeans",
        "category": "jeans",
        "price": 99.99,
        "description": "A Blue Jeans",
    }
    created_product = create_product_via_api(client, **create_payload)

    patch_payload = {
        "name": "Light Blue Jeans",
        "description": "A Light Blue Jeans",
    }
    patch_response = client.patch(
        f"/products/{created_product['id']}", json=patch_payload
    )
    assert patch_response.status_code == 200

    patched_product = patch_response.json()
    assert patched_product["name"] == patch_payload["name"]
    assert patched_product["description"] == patch_payload["description"]

    patch_payload = {"price": 199.99}
    patch_response = client.patch(
        f"/products/{created_product['id']}", json=patch_payload
    )
    assert patch_response.status_code == 200

    patched_product = patch_response.json()
    assert patched_product["price"] == patch_payload["price"]

    patch_payload = {"category": "t-shirts"}
    patch_response = client.patch(
        f"/products/{created_product['id']}", json=patch_payload
    )
    assert patch_response.status_code == 200

    patched_product = patch_response.json()
    assert patched_product["category"] == patch_payload["category"]


def test_patch_update_product__wrong_values(client):
    create_payload = {
        "name": "Blue Jeans",
        "category": "jeans",
        "price": 99.99,
        "description": "A Blue Jeans",
    }
    created_product = create_product_via_api(client, **create_payload)

    patch_payload = {"price": -10.0}
    patch_response = client.patch(
        f"/products/{created_product['id']}", json=patch_payload
    )
    assert patch_response.status_code == 422
    body = patch_response.json()
    assert any(err["loc"][-1] == "price" for err in body["detail"])

    patch_payload = {"price": "not-a-number"}
    patch_response = client.patch(
        f"/products/{created_product['id']}", json=patch_payload
    )
    assert patch_response.status_code == 422
    body = patch_response.json()
    assert any(err["loc"][-1] == "price" for err in body["detail"])

    patch_payload = {"category": "non-existent-category"}
    patch_response = client.patch(f"/products/{created_product['id']}", json=patch_payload)
    assert patch_response.status_code == 400
    body = patch_response.json()
    assert body["detail"] == "Invalid Category"
    
    patch_payload = {"name": "New Name"}
    patch_response = client.patch("/products/invalid-uuid", json=patch_payload)
    assert patch_response.status_code == 422
    body = patch_response.json()
    assert body["detail"][0]["type"] == "uuid_parsing"
    


def test_patch_product_not_found(client):
    update_payload = {
        "name": "Yellow T-Shirt",
        "category": "t-shirts",
        "price": 199.99,
        "description": "A Yellow T-Shirt",
    }
    fake_id = uuid.uuid4()
    assert client.patch(f"/products/{fake_id}", json=update_payload).status_code == 404
