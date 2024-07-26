import unittest
from datetime import timedelta
from io import StringIO
from unittest.mock import patch, mock_open

from script.modules.display_and_save import display_output
from script.modules.display_and_save import save_results_in_json


class TestDisplayOutput(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_output(self, mock_stdout):
        data = [
            {
                "number": "1",
                "name": "John",
                "surname": "Doe",
                "result": timedelta(seconds=10)
            }
        ]
        display_output(data)
        output = mock_stdout.getvalue()
        print(output)
        self.assertIn("Занятое место", output)
        self.assertIn("1", output)
        self.assertIn("John", output)
        self.assertIn("Doe", output)

    @patch("sys.stderr", new_callable=StringIO)
    def test_display_output_missing_key(self, mock_stderr):
        data = [
            {
                "number": "1",
                "name": "John",
                # Missing 'surname' and 'result'
            }
        ]
        display_output(data)
        error_output = mock_stderr.getvalue()
        self.assertIn("Key missing trying parse data for displaying",
                      error_output)


class TestSaveResultsToJson(unittest.TestCase):
    def setUp(self) -> None:
        self.res = [
            timedelta(minutes=2, seconds=32, milliseconds=500),
            timedelta(minutes=5, seconds=12, milliseconds=320)
        ]
        self.results = [
            {"number": "1", "surname": "Doe", "name": "John",
             "result": self.res[0]},
            {"number": "2", "surname": "Smith", "name": "Jane",
                "result": self.res[1]}
                ]
        self.path = "test_output.json"

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_save_results_in_json_valid(self, mock_json_dump, mock_open):
        save_results_in_json(self.results, self.path)
        mock_open.assert_called_once_with(self.path, "w", encoding="utf-8")

        args, _ = mock_json_dump.call_args
        saved_data = args[0]

        self.assertEqual(len(saved_data), 2)
        self.assertIn("1", saved_data)
        self.assertIn("2", saved_data)

        self.assertEqual(saved_data["1"]["Нагрудный номер"], "1")
        self.assertEqual(saved_data["1"]["Имя"], "Doe")
        self.assertEqual(saved_data["1"]["Фамилия"], "John")
        self.assertEqual(saved_data["1"]["Результат"], "02:32,05")

        self.assertEqual(saved_data["2"]["Нагрудный номер"], "2")
        self.assertEqual(saved_data["2"]["Имя"], "Smith")
        self.assertEqual(saved_data["2"]["Фамилия"], "Jane")
        self.assertEqual(saved_data["2"]["Результат"], "05:12,03")


if __name__ == "__main__":
    unittest.main()
