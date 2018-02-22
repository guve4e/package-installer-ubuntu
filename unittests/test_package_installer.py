from unittest import TestCase

from src.package_installer import PackageInstaller


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

        self.package = PackageInstaller(self.package_list)

    def runTest(self):
        self.test_proper_initialization

    def test_found_char(self):
        # Arrange
        version = "'b'64.0.3282.167-0ubuntu0.17.10.1''"
        # Act
        result = self.package.found_char(version, "t")
        # Assert
        self.assertTrue(True, result)

    def test_split_string(self):
        # Arrange
        test_string = "1111111!000000"
        # Act
        actual = self.package.split_string(test_string, "!")
        # Assert
        self.assertEqual("1111111", actual)

    def test_sanitize_string(self):
        # Arrange
        test_string = "'b'64.0.3282.167-0ubuntu0.17.10.1''"
        expected_string = "64.0.3282.167-0ubuntu0.17.10.1"
        # Act
        actual_string = self.package.sanitize_str(test_string)
        # Assert
        self.assertEqual(expected_string, actual_string)

    def test_remove_chars(self):
        # Arrange
        test_string = "'b'64.0.3282.167-0ubuntu0.17.10.1''"
        expected_string = "64.0.3282.167"
        # Act
        actual_string = self.package.remove_chars(test_string)
        # Assert
        self.assertEqual(expected_string, actual_string)


    # def test_initialization_with_text_file(self):
    #     # Arrange
    #     expected_list = [
    #         {
    #             "name": "Chromium-Browser",
    #             "comment": "No comment",
    #             "package name": "chromium-browser",
    #             "version": "Latest",
    #             "commands": [
    #                 {
    #                     "commandDescription": "install",
    #                     "command": "sudo apt-get install chromium-browser -y"
    #                 }
    #             ]
    #         },
    #         {
    #             "name": "Kdeconnect",
    #             "comment": "No Comment",
    #             "package name": "kdeconnect",
    #             "version": "Latest",
    #             "commands": [
    #                 {
    #                     "commandDescription": "install",
    #                     "command": "sudo apt install kdeconnect -y"
    #                 }
    #             ]
    #         }
    #     ]
    #
    #     # Act
    #     package = PackageInstaller("testPackageInstaller.txt")
    #
    #     # Assert
    #     self.assertEqual(expected_list, package.packages)
    #
    # def test_initialization_with_json_file(self):
    #     # Arrange
    #
    #
    #     package = PackageInstaller("testPackageInstaller.json")
    #
    #     self.assertEqual(expectet_list, package.packages)
    #
    # def foo(self):
    #     # Arrange
    #
    #     # Act
    #
    #     # Assert
    #
    #     self.assertEqual()