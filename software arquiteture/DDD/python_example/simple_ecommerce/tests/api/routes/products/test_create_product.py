import pytest
from tests.utils import create_product_via_api


def test_create_product(client):
    res = create_product_via_api(client, name="Blue Jeans", category="jeans", price=99.99, description="A Blue Jeans")    
    assert "id" in res
    assert res["name"] == "Blue Jeans"
    assert res["category"] == "jeans"
    assert float(res["price"]) == pytest.approx(99.99)
    assert res["description"] == "A Blue Jeans"
    
    
def test_create_product_wrong_values_raises(client): ...


def test_create_product_sqlinjection_raises(client): ...
