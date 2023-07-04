import os
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase


class TestRunner(TestCase):
    """Boilerplate code to add tests to"""

    def test_change_file_permissions(self):
        for expected_mode in [0o100600, 0o100644, 0o100660]:
            with self.subTest(expected_mode):
                with TemporaryDirectory() as tmp_dir:
                    file_path = Path(tmp_dir) / "test.yaml"
                    file_path.write_bytes(b"")
                    os.chmod(str(file_path), expected_mode)
                    self.assertEqual(
                        file_path.stat().st_mode, expected_mode
                    )
