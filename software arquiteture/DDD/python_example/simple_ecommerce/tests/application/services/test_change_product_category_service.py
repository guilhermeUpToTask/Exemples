import pytest
from src.domain.catalog.value_objects.product_value_objects import (
    CategoryName,
    ProductName,
    ProductId,
)
from src.domain.shared.value_objects import Price
from src.domain.catalog.entities.product import Product


def test_change_product_category_success(
    change_product_category_service, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    change_product_category_service.execute(sample_product, "t-shirts")
    assert sample_product.category.value == "t-shirts"


def test_change_product_category_wrong_value(
    change_product_category_service, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    with pytest.raises(ValueError):
        change_product_category_service.execute(sample_product, "wrong category")


def test_change_product_category_empty_name_raise(
    change_product_category_service, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    with pytest.raises(ValueError):
        change_product_category_service.execute(sample_product, "")


def test_change_product_category_product_not_found_raises(
    change_product_category_service, sample_product
):
    with pytest.raises(ValueError):
        change_product_category_service.execute(sample_product, "t-shirts")
