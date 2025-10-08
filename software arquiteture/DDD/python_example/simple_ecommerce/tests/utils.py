from fastapi.testclient import TestClient


def create_product_via_api(
    client: TestClient,
    name: str = "Sample",
    category: str = "default",
    price: float = 10.5,
    description: str = "desc",
):
    payload = {
        "name": name,
        "category": category,
        "price": price,
        "description": description,
    }
    r = client.post("/products/", json=payload)
    assert r.status_code == 200, f"create failed: {r.status_code} {r.text}"
    return r.json()
