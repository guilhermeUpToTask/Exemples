import uuid
from tests.utils import create_product_via_api


def test_delete_product_success(client):
    res = create_product_via_api(
        client=client,
        name="Blue Jeans",
        category="jeans",
        price=99.99,
        description="A Blue Jeans",
    )
    assert client.delete(f"/products/{res["id"]}").status_code == 204
    assert client.get(f"/products/{res["id"]}").status_code == 404


def test_delete_product_not_found_raises(client):
    assert client.delete(f"/products/{uuid.uuid4()}").status_code == 404
