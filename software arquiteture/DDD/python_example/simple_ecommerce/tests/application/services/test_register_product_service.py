import pytest


def test_register_product_success(register_service, catalog_uow):
    product = register_service.execute(name="Blue Jeans", category="jeans", price=200.0)
    # Should be in the repository
    assert catalog_uow.products.get_by_id(product.id) == product
    assert product.name.value == "Blue Jeans"
    assert product.price.amount == 200.0


def test_register_product_invalid_price_raises(register_service):
    with pytest.raises(ValueError):
        register_service.execute(name="Blue Jeans", category="jeans", price=-100)
