import pytest

from src.domain.shared.value_objects import Price
from src.domain.catalog.value_objects.product_value_objects import ProductName


def test_add_and_get_by_id(sqlmodel_product_repo, sample_product):
    sqlmodel_product_repo.add(sample_product)
    fetched = sqlmodel_product_repo.get_by_id(sample_product.id)
    assert fetched is not None
    assert fetched.name.value == sample_product.name.value
    assert fetched.price.amount == sample_product.price.amount


def test_list_all(sqlmodel_product_repo, sample_product):
    sqlmodel_product_repo.add(sample_product)
    all_products = sqlmodel_product_repo.list_all()
    assert len(all_products) == 1
    assert all_products[0].id == sample_product.id


def test_list_by_category(sqlmodel_product_repo, sample_product):
    sqlmodel_product_repo.add(sample_product)
    result = sqlmodel_product_repo.list_by_category(sample_product.category)
    assert len(result) == 1
    assert result[0].category.value == sample_product.category.value


def test_update(sqlmodel_product_repo, sample_product):
    sqlmodel_product_repo.add(sample_product)

    sample_product.name = ProductName("Updated Name")
    sample_product.price = Price(199.99)

    updated = sqlmodel_product_repo.update(sample_product)
    assert updated.name.value == "Updated Name"
    assert updated.price.amount == 199.99


def test_delete(sqlmodel_product_repo, sample_product):
    sqlmodel_product_repo.add(sample_product)
    sqlmodel_product_repo.delete(sample_product.id)
    sqlmodel_product_repo.flush()

    assert sqlmodel_product_repo.get_by_id(sample_product.id) is None
