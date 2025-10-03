from typing import List
import pytest
from src.domain.catalog.value_objects.product_value_objects import (
    ProductId,
)


def test_change_product_price_success(
    change_product_price_service, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    change_product_price_service.execute(sample_product, 100.5)
    assert sample_product.price.amount == 100.5


def test_change_product_invalid_price_raises(
    change_product_price_service, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    with pytest.raises(ValueError):
        change_product_price_service.execute(sample_product, -20.5)


def test_change_product_not_found_raises(
    change_product_price_service, sample_product
):
    missing_product = sample_product
    with pytest.raises(ValueError):
        change_product_price_service.execute(missing_product, 100.5)
