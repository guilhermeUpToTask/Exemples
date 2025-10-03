import pytest
from src.api.schemas.products import SimpleProductUpdate


def test_update_product_simples_fields_success(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    update_product_simple_fields_services.execute(
        sample_product, SimpleProductUpdate(name="Light Blue Jeans")
    )
    assert sample_product.name.value == "Light Blue Jeans"
    update_product_simple_fields_services.execute(
        sample_product, SimpleProductUpdate(description="A Light Blue Jeans")
    )
    assert sample_product.description == "A Light Blue Jeans"
    update_product_simple_fields_services.execute(
        sample_product,
        SimpleProductUpdate(name="Black Jeans", description="A Black Blue Jeans"),
    )
    assert sample_product.name.value == "Black Jeans"
    assert sample_product.description == "A Black Blue Jeans"


def test_update_product_simple_fields_empty_name(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    with pytest.raises(ValueError):
        update_product_simple_fields_services.execute(
            sample_product, SimpleProductUpdate(name="")
        )


def test_update_product_simple_fields_product_missing_raises(
    update_product_simple_fields_services, sample_product
):
    missing_product = sample_product
    with pytest.raises(ValueError):
        update_product_simple_fields_services.execute(
            missing_product, SimpleProductUpdate(name="Light Blue Jeans")
        )


def test_update_product_simple_fields_noop(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    original_name = sample_product.name
    update_product_simple_fields_services.execute(sample_product, SimpleProductUpdate())
    assert sample_product.name == original_name


def test_update_product_simple_fields_invalid_name(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    with pytest.raises(ValueError):
        update_product_simple_fields_services.execute(
            sample_product, SimpleProductUpdate(name="X" * 101)
        )


def test_update_product_description_none_raises(
    update_product_simple_fields_services, catalog_uow, sample_product
):
    catalog_uow.products.add(sample_product)
    with pytest.raises(ValueError):
        update_product_simple_fields_services.execute(
            sample_product, SimpleProductUpdate(description=None)
        )
