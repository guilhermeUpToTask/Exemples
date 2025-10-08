import pytest
from src.domain.catalog.value_objects.product_value_objects import InvalidDescription, InvalidProductName


def test_update_product_simples_fields_success(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    update_product_simple_fields_services.execute(
        product=sample_product, new_name="Light Blue Jeans"
    )
    assert sample_product.name.value == "Light Blue Jeans"

    update_product_simple_fields_services.execute(
        product=sample_product, new_description="A Light Blue Jeans"
    )
    assert sample_product.description.value == "A Light Blue Jeans"

    update_product_simple_fields_services.execute(
        product=sample_product,
        new_name="Black Jeans",
        new_description="A Black Blue Jeans",
    )
    assert sample_product.name.value == "Black Jeans"
    assert sample_product.description.value == "A Black Blue Jeans"


def test_update_product_simple_fields_empty_name_raises(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    with pytest.raises(InvalidProductName):
        update_product_simple_fields_services.execute(
            product=sample_product, new_name=""
        )
def test_update_product_simples_fields_empty_description_raises(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    with pytest.raises(InvalidDescription):
        update_product_simple_fields_services.execute(
            product=sample_product, new_description=""
        )


def test_update_product_simple_fields_product_missing_raises(
    update_product_simple_fields_services, sample_product
):
    missing_product = sample_product
    #TODO: create ProductNotFound Error
    with pytest.raises(ValueError):
        update_product_simple_fields_services.execute(
            product=missing_product, new_name="Light Blue Jeans"
        )


def test_update_product_simple_fields_noop(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    original_name = sample_product.name
    update_product_simple_fields_services.execute(product=sample_product)
    assert sample_product.name == original_name


def test_update_product_simple_fields_invalid_name(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    with pytest.raises(InvalidProductName):
        update_product_simple_fields_services.execute(
            product=sample_product, new_name="X" * 101
        )