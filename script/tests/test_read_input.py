import unittest
from datetime import datetime
from unittest.mock import patch, mock_open


from script.modules.read_input import load_competitors_from_json
from script.modules.read_input import load_results_from_txt


class TestLoadCompetitorsFromJson(unittest.TestCase):
    def test_load_competitors_from_json_valid(self):
        mock_json = '{"1": {"name": "John", "surname": "Doe"}}'
        with patch("builtins.open", mock_open(read_data=mock_json)):
            competitors = load_competitors_from_json("path/to/file.json")
            self.assertEqual(
                competitors, {'1': {'name': 'John', 'surname': 'Doe'}}
                )

    def test_load_competitors_from_json_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            competitors = load_competitors_from_json('path/to/nonex/file.json')
            self.assertEqual(competitors, {})

    def test_load_competitors_from_json_bad_json(self):
        invalid_data = '{"1": {"name": "John" "surname": "Doe"}}'
        with patch("builtins.open", mock_open(read_data=invalid_data)):
            competitors = load_competitors_from_json("path/to/bad/file.json")
            self.assertEqual(competitors, {})


class TestLoadResults(unittest.TestCase):
    def test_load_results_from_txt_valid(self):
        mock_data = "1 start 12:00:00,000\n1 finish 12:30:00,000\n"
        expected = {
                1: {
                    "start": datetime.strptime("12:00:00,000", "%H:%M:%S,%f"),
                    "finish": datetime.strptime("12:30:00,000", "%H:%M:%S,%f")
                }
            }
        with patch("builtins.open", mock_open(read_data=mock_data)):
            results = load_results_from_txt("path/file.txt")
            self.assertEqual(results, expected)

    def test_load_results_from_txt_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            results = load_results_from_txt('path/not/exist.txt')
            self.assertEqual(results, {})

    def test_load_results_from_txt_invalid_line(self):
        invalid_data = "1 start 12:00:00,000\ninvalid_line\n"
        with patch("builtins.open", mock_open(read_data=invalid_data)):
            results = load_results_from_txt("path/to/file.txt")
            self.assertEqual(results, {})


if __name__ == "__main__":
    unittest.main()
