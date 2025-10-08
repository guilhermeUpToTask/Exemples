class DomainError(Exception):
    """Base class for all domain-related errors."""

    pass


class InvalidValue(DomainError, ValueError):
    """Invalid value for a value object."""
