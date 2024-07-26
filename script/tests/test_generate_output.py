import unittest
from datetime import timedelta, datetime

from script.modules.generate_output import calculate_durations
from script.modules.generate_output import generate_output


class TestCalculateDurations(unittest.TestCase):
    def test_calculate_durations_valid(self):
        input = {
                1: {
                    "start": datetime.strptime("12:00:00,000", "%H:%M:%S,%f"),
                    "finish": datetime.strptime("12:30:00,000", "%H:%M:%S,%f")
                }
            }
        expect = {
            1: timedelta(minutes=30)
            }
        durations = calculate_durations(input)
        self.assertEqual(durations, expect)


class TestGenerateOutput(unittest.TestCase):
    def test_generate_output_valid(self):
        competitors = {
            '1': {'Name': 'John', 'Surname': 'Doe'},
            '2': {'Name': 'Jane', 'Surname': 'Doe'}
        }
        durations = {
            1: timedelta(hours=1, minutes=20),
            2: timedelta(hours=1, minutes=10)
        }
        expected_output = [
            {
                'number': '2',
                'name': 'Jane',
                'surname': 'Doe',
                'result': timedelta(hours=1, minutes=10)
            },
            {
                'number': '1',
                'name': 'John',
                'surname': 'Doe',
                'result': timedelta(hours=1, minutes=20)
            }
        ]
        output = generate_output(competitors, durations)
        print(output)
        self.assertEqual(output, expected_output)

    def test_generate_output_missing_duration(self):
        competitors = {
            '1': {'Name': 'John', 'Surname': 'Doe'},
            '2': {'Name': 'Jane', 'Surname': 'Doe'}
        }
        durations = {
            1: timedelta(hours=1, minutes=20)
        }
        expected_output = [
            {
                'number': '1',
                'name': 'John',
                'surname': 'Doe',
                'result': timedelta(hours=1, minutes=20)
            }
        ]
        output = generate_output(competitors, durations)
        self.assertEqual(output, expected_output)

    def test_generate_output_invalid_number(self):
        competitors = {
            '1\uFEFF': {'Name': 'John', 'Surname': 'Doe'},
            '2': {'Name': 'Jane', 'Surname': 'Doe'}
        }
        durations = {
            1: timedelta(hours=1, minutes=20),
            2: timedelta(hours=1, minutes=10)
        }
        expected_output = [
            {
                'number': '2',
                'name': 'Jane',
                'surname': 'Doe',
                'result': timedelta(hours=1, minutes=10)
            },
            {
                'number': '1',
                'name': 'John',
                'surname': 'Doe',
                'result': timedelta(hours=1, minutes=20)
            }
        ]
        output = generate_output(competitors, durations)
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
