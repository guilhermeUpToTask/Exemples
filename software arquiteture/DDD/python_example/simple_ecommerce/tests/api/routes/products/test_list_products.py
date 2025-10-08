from tests.utils import create_product_via_api


def create_sample_products(client):
    """Create a few sample products for testing list endpoints."""
    products = [
        {"name": "Blue Jeans", "category": "jeans", "price": 99.99, "description": "A Blue Jeans"},
        {"name": "Red Shirt", "category": "t-shirts", "price": 49.99, "description": "A Red Shirt"},
        {"name": "Black Jeans", "category": "jeans", "price": 129.99, "description": "A Black Jeans"},
        {"name": "Yellow T-Shirt", "category": "t-shirts", "price": 19.99, "description": "A Yellow T-Shirt"},
    ]
    created = []
    for p in products:
        created.append(create_product_via_api(client, **p))
    return created


def test_list_products(client):
    create_sample_products(client)
    
    response = client.get("/products/")
    assert response.status_code == 200

    products = response.json()
    assert len(products) >= 4
    names = [p["name"] for p in products]
    assert "Blue Jeans" in names
    assert "Red Shirt" in names


def test_list_products_with_filters(client):
    create_sample_products(client)
    
    response = client.get("/products/?category=jeans")
    assert response.status_code == 200
    products = response.json()
    assert all(p["category"] == "jeans" for p in products)
    assert len(products) == 2

    response = client.get("/products/?min_price=100")
    assert response.status_code == 200
    products = response.json()
    assert all(p["price"] >= 100 for p in products)

    response = client.get("/products/?max_price=50")
    assert response.status_code == 200
    products = response.json()
    assert all(p["price"] <= 50 for p in products)

    response = client.get("/products/?category=t-shirts&min_price=10&max_price=50")
    assert response.status_code == 200
    products = response.json()
    assert all(p["category"] == "t-shirts" and 10 <= p["price"] <= 50 for p in products)


def test_list_products_wrong_filters_raises(client):
    response = client.get("/products/?min_price=not-a-number")
    assert response.status_code == 422
    body = response.json()
    assert any(err["loc"][-1] == "min_price" for err in body["detail"])

    response = client.get("/products/?max_price=abc")
    assert response.status_code == 422
    body = response.json()
    assert any(err["loc"][-1] == "max_price" for err in body["detail"])
