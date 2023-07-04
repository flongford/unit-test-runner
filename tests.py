import os
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase


class TestRunner(TestCase):
    """Boilerplate code to add tests to"""

    def test_change_file_permissions(self):
        with TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.yaml"
            file_path.write_bytes(b"")

            expected_mode = 0o100660
            os.chmod(str(file_path), expected_mode)

            self.assertEqual(file_path.stat().st_mode, expected_mode)
