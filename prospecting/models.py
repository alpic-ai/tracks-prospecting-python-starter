from dataclasses import dataclass


@dataclass(frozen=True)
class SearchRequest:
    countries: tuple[str, ...]
    industry: str
    min_employees: int
    max_employees: int
    roles: tuple[str, ...]
    limit: int

    def __post_init__(self):
        if not self.countries or not self.roles or not self.industry.strip():
            raise ValueError("Countries, industry and roles are required")
        if self.min_employees < 1 or self.max_employees < self.min_employees:
            raise ValueError("Invalid employee range")
        if self.limit < 1:
            raise ValueError("Limit must be positive")


@dataclass(frozen=True)
class Contact:
    name: str
    title: str
    company: str
    country: str
    work_email: str
    verification_status: str
