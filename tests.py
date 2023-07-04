import os
import stat
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase


class TestRunner(TestCase):
    """Boilerplate code to add tests to"""

    def test_change_file_permissions_chmod(self):
        for expected_mode in [0o666, 0o644, 0o600]:
            with self.subTest(expected_mode):
                with TemporaryDirectory() as tmp_dir:
                    file_path = Path(tmp_dir) / f"{expected_mode}.yaml"
                    file_path.touch()

                    os.chmod(str(file_path), expected_mode)

                    actual_mode = stat.S_IMODE(file_path.stat().st_mode)

                    self.assertEqual(
                        actual_mode, expected_mode,
                        msg=f"{stat.filemode(actual_mode)} != {stat.filemode(expected_mode)}"
                    )

    def test_change_file_permissions_touch(self):
        for expected_mode in [0o644, 0o600]:
            with self.subTest(expected_mode):
                with TemporaryDirectory() as tmp_dir:
                    file_path = Path(tmp_dir) / f"{expected_mode}.yaml"
                    file_path.touch(expected_mode)

                    actual_mode = stat.S_IMODE(file_path.stat().st_mode)

                    self.assertEqual(
                        actual_mode, expected_mode,
                        msg=f"{stat.filemode(actual_mode)} != {stat.filemode(expected_mode)}"
                    )
