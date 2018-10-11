from unittest import TestCase
from unittest.mock import MagicMock

from src.package_installer import PackageInstaller
from src.bash_connector import BashConnector


class TestPackageInstaller(TestCase):

    def setUp(self):
        self.package_list = [
            {
                "name": "Chrome",
                "comment": "Chrome Installer",
                "package name": "chromium-browser",
                "version": "Latest",
                "commands": [
                    {
                        "commandDescription": "install",
                        "command": "sudo apt-get install chromium-browser -y"
                    }
                ]
            },
            {
                "name": "KDE-Connect",
                "comment": "Kde-Connect Installer",
                "package name": "kdeconnect",
                "version": "Latest",
                "commands": [
                    {
                        "commandDescription": "repository",
                        "command": "sudo add-apt-repository ppa:varlesh-l/indicator-kdeconnect"
                    },
                    {
                        "commandDescription": "update",
                        "command": "sudo apt update"
                    },
                    {
                        "commandDescription": "search and replace make adjustments",
                        "command": "sudo sed -i 's/yakkety/xenial/g' /etc/apt/sources.list.d/varlesh-l-ubuntu-indicator-kdeconnect-yakkety.list"
                    },
                    {
                        "commandDescription": "install",
                        "command": "sudo apt install kdeconnect indicator-kdeconnect -y"
                    }
                ]
            }
        ]

        self.mockAptCache = b'apache7:\n' \
                 b'Installed: 2.4.27-2ubuntu4.2\n' \
                 b'Candidate: 2.4.27-2ubuntu4.2\n' \
                 b'Version table:\n' \
                 b'*** 2.4.27-2ubuntu4.2 500\n' \
                 b'500 http://us.archive.ubuntu.com/ubuntu artful-updates/main amd64 Packages\n' \
                 b'100 /var/lib/dpkg/status\n' \
                 b'2.4.27-2ubuntu4.1 500\n' \
                 b'500 http://security.ubuntu.com/ubuntu artful-security/main amd64 Packages\n' \
                 b'2.4.27-2ubuntu3 500\n' \
                 b'500 http://us.archive.ubuntu.com/ubuntu artful/main amd64 Packages\n'

        self.mockBashConnector = BashConnector()
        self.mockBashConnector.apt_cache = MagicMock(return_value=self.mockAptCache)
        self.mockBashConnector.install_package = MagicMock()
        self.mockBashConnector.update = MagicMock()

        self.package = PackageInstaller(self.mockBashConnector, self.package_list)

    def runTest(self):
        self.test_found_char()
        self.test_split_string()
        self.test_sanitize_string()
        self.test_remove_chars()


    def test_found_char(self):
        # Arrange
        param_list = [("'b'64.0.3282.167-0ubuntu0.17.10.1''", True), ("nowhere", False)]

        # Act
        for parameter, expected in param_list:
            with self.subTest():
                actual_result = self.package.found_char(parameter, "t")
                # Assert
                self.assertEqual(actual_result, expected)

    def test_split_string(self):
        # Arrange
        param_list =[
            ("1111111!000000", "1111111"),
            ("somestring!someotherstring", "somestring")
        ]

        # Act
        for parameter, expected in param_list:
            with self.subTest():
                actual_result = self.package.split_string(parameter, "!")
                # Assert
                self.assertEqual(actual_result, expected)

    def test_sanitize_string(self):
        # Arrange
        param_list = [
            ("'b'64.0.3282.167-0ubuntu0.17.10.1''", "64.0.3282.167-0ubuntu0.17.10.1"),
            ("'b'somestring", "somestring")
        ]

        # Act
        for parameter, expected in param_list:
            with self.subTest():
                actual = self.package.sanitize_str(parameter)
                # Assert
                self.assertEqual(expected, actual)

    def test_remove_chars(self):
        # Arrange
        test_string = "'b'64.0.3282.167-0ubuntu0.17.10.1''"
        expected_string = "64.0.3282.167"

        # Act
        actual_string = self.package.remove_chars(test_string)

        # Assert
        self.assertEqual(expected_string, actual_string)
