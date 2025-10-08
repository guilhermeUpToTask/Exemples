from src.application.catalog.dtos.product_dtos import ProductFilter
from src.domain.shared.specifications import FieldSpecification, AndSpecification
from src.domain.catalog.specifications.product_specifications import available_products


def map_filters_to_spec(filters: ProductFilter):
    specs = []
    if filters.min_price is not None:
        specs.append(FieldSpecification("price", "gt", filters.min_price))
    if filters.max_price is not None:
        specs.append(FieldSpecification("price", "lt", filters.max_price))
    if filters.category:
        specs.append(FieldSpecification("category", "eq", filters.category))

    if not specs:
        return None

    if len(specs) == 1:
        return specs[0]

    return AndSpecification(*specs)
