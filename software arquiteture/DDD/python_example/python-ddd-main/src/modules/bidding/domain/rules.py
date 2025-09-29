from datetime import datetime, timedelta

from pydantic import Field

from seedwork.domain.rules import BusinessRule
from seedwork.domain.value_objects import Money


class PriceOfPlacedBidMustBeGreaterOrEqualThanNextMinimumPrice(BusinessRule):
    __message = "Placed bid must be greater or equal than {next_minimum_price}"

    current_price: Money
    next_minimum_price: Money

    def is_broken(self) -> bool:
        return self.current_price < self.next_minimum_price

    def get_message(self) -> str:
        return self.__message.format(next_minimum_price=self.next_minimum_price)


class BidCanBeRetracted(BusinessRule):
    __message = "Bid cannot be retracted"

    listing_ends_at: datetime
    bid_placed_at: datetime
    now: datetime = Field(default_factory=datetime.utcnow)

    def is_broken(self) -> bool:
        time_left_in_listing = self.now - self.listing_ends_at
        time_since_placed = self.now - self.bid_placed_at
        less_than_12_hours_before_bidding_ends = time_left_in_listing < timedelta(
            hours=12
        )
        less_than_1_hour_since_bid_was_placed = time_since_placed < timedelta(hours=1)

        return (
            less_than_12_hours_before_bidding_ends
            and less_than_1_hour_since_bid_was_placed
        )


class ListingCanBeCancelled(BusinessRule):
    __message = "Listing cannot be cancelled"

    time_left_in_listing: timedelta
    no_bids_were_placed: int

    def is_broken(self) -> bool:
        can_be_cancelled = self.time_left_in_listing > timedelta(hours=12) or (
            self.time_left_in_listing <= timedelta(hours=12)
            and self.no_bids_were_placed
        )
        return not can_be_cancelled
