import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from prospecting.csv_output import write_contacts
from prospecting.models import Contact, SearchRequest


class ScaffoldTests(unittest.TestCase):
    def test_export_keeps_more_than_ten_rows_and_uncertain_results(self):
        # Synthetic records exercise serialization only, never live enrichment.
        rows = [
            Contact(f"Fixture {i}", "VP of Sales", 'Example, Inc.', "France",
                    "" if i == 11 else f"fixture-{i}@example.test",
                    "NOT_FOUND" if i == 11 else ("CATCH_ALL" if i == 10 else "DELIVERABLE"))
            for i in range(12)
        ]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nested" / "contacts.csv"
            self.assertEqual(write_contacts(path, rows), 12)
            with path.open(encoding="utf-8", newline="") as stream:
                result = list(csv.DictReader(stream))
        self.assertEqual(len(result), 12)
        self.assertEqual(result[0]["company"], "Example, Inc.")
        self.assertEqual(result[10]["verification_status"], "CATCH_ALL")
        self.assertEqual(result[11]["work_email"], "")
        self.assertEqual(result[11]["verification_status"], "NOT_FOUND")

    def test_invalid_request_is_rejected(self):
        with self.assertRaises(ValueError):
            SearchRequest(("France",), "Software Development", 500, 51, ("VP of Sales",), 12)

    def test_invalid_cli_request_does_not_create_an_output(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "contacts.csv"
            result = subprocess.run(
                [sys.executable, "-m", "prospecting", "--countries", "France",
                 "--industry", "Software Development", "--min-employees", "500",
                 "--max-employees", "51", "--roles", "VP of Sales",
                 "--output", str(output)],
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 2)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
