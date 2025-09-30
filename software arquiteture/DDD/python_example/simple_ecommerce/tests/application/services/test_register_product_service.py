import pytest
def test_register_product_success(register_service, fake_repo):
    product = register_service.execute(
        id="p1", name="Blue Jeans", category="jeans", price=200.0
    )
    # Should be in the repository
    assert fake_repo.get_by_id("p1") == product
    assert product.name.value == "Blue Jeans"
    assert product.price.amount == 200.0


def test_register_product_invalid_price_raises(register_service):
    with pytest.raises(ValueError):
        register_service.execute(
            id="p2", name="Blue Jeans", category="jeans", price=-100
        )
