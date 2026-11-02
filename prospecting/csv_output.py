import csv
from dataclasses import asdict, fields
from pathlib import Path
from typing import Iterable

from .models import Contact


def write_contacts(path: Path, contacts: Iterable[Contact]) -> int:
    rows = list(contacts)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=[field.name for field in fields(Contact)])
        writer.writeheader()
        writer.writerows(asdict(contact) for contact in rows)
    return len(rows)
