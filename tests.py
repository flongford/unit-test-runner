import os
import stat
from pathlib import Path
from tempfile import mkstemp
from unittest import TestCase


class TestRunner(TestCase):
    """Boilerplate code to add tests to"""

    def test_change_file_permissions_chmod(self):
        expected_mode = 0o100666
        tmp_file_fd, tmp_file_path = mkstemp(suffix="file.yaml")
        os.close(tmp_file_fd)
        tmp_file_path = Path(tmp_file_path)

        tmp_file_path.chmod(expected_mode)

        actual_mode = tmp_file_path.stat().st_mode
        self.assertEqual(
            actual_mode, expected_mode,
            msg=f"{stat.filemode(actual_mode)} != {stat.filemode(expected_mode)}"
        )
