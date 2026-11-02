import argparse
import sys
from pathlib import Path

from .csv_output import write_contacts
from .models import SearchRequest
from .provider import collect_contacts


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a prospect list with a live data provider")
    parser.add_argument("--countries", nargs="+", required=True)
    parser.add_argument("--industry", required=True)
    parser.add_argument("--min-employees", type=int, required=True)
    parser.add_argument("--max-employees", type=int, required=True)
    parser.add_argument("--roles", nargs="+", required=True)
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--output", type=Path, default=Path("results/prospects.csv"))
    args = parser.parse_args()
    try:
        request = SearchRequest(
            countries=tuple(args.countries),
            industry=args.industry,
            min_employees=args.min_employees,
            max_employees=args.max_employees,
            roles=tuple(args.roles),
            limit=args.limit,
        )
        contacts = collect_contacts(request)
        count = write_contacts(args.output, contacts)
    except (ValueError, NotImplementedError) as error:
        print(str(error), file=sys.stderr)
        return 2
    print(f"Wrote {count} rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
