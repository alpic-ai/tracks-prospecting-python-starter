from .models import Contact, SearchRequest


def collect_contacts(request: SearchRequest) -> list[Contact]:
    """Implement live search, the required approval flow and enrichment here.

    Returning synthetic contacts or guessing missing emails does not implement
    this adapter. Read the task for the provider and required behavior.
    """
    raise NotImplementedError("Live provider integration has not been implemented")
