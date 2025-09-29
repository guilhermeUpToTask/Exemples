import pytest

from modules.catalog.application.command.publish_listing_draft import (
    PublishListingDraftCommand,
    publish_listing_draft,
)
from modules.catalog.domain.entities import Listing, Seller
from modules.catalog.domain.value_objects import ListingStatus
from seedwork.domain.exceptions import BusinessRuleValidationException
from seedwork.domain.value_objects import Money
from seedwork.infrastructure.repository import InMemoryRepository


@pytest.mark.unit
@pytest.mark.asyncio
async def test_publish_listing():
    # arrange
    seller_repository = InMemoryRepository()
    seller = Seller(id=Seller.next_id())
    seller_repository.add(seller)

    listing_repository = InMemoryRepository()
    listing = Listing(
        id=Listing.next_id(),
        title="Tiny dragon",
        description="Tiny dragon for sale",
        ask_price=Money(1),
        seller_id=seller.id,
    )
    listing_repository.add(listing)

    command = PublishListingDraftCommand(
        listing_id=listing.id,
        seller_id=seller.id,
    )

    # act
    await publish_listing_draft(
        command,
        listing_repository=listing_repository,
    )

    # assert
    assert listing.status == ListingStatus.PUBLISHED


@pytest.mark.unit
@pytest.mark.asyncio
async def test_publish_listing_and_break_business_rule():
    # arrange
    seller_repository = InMemoryRepository()
    seller = Seller(id=Seller.next_id())
    seller_repository.add(seller)

    listing_repository = InMemoryRepository()
    listing = Listing(
        id=Listing.next_id(),
        title="Tiny dragon",
        description="Tiny dragon for sale",
        ask_price=Money(0),  # this will break the rule
        seller_id=seller.id,
    )
    listing_repository.add(listing)

    command = PublishListingDraftCommand(
        listing_id=listing.id,
        seller_id=seller.id,
    )

    # act

    # assert
    with pytest.raises(BusinessRuleValidationException):
        await publish_listing_draft(
            command,
            listing_repository=listing_repository,
        )
