import unittest
from days_in_month import days_in_month

class TestDaysInMonth(unittest.TestCase):
    # Check that month has specific amount of days
    def test_valid_month(self):
        self.assertEqual(days_in_month("January"), 31)
    
    # The same, but we expect an error now (because February can't have less than 28 days)
    @unittest.expectedFailure
    def test_incorrect_data_expected(self):
        self.assertLess(days_in_month("February"), 28)
    
    # Check the exception
    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            days_in_month("InvalidMonth")

    # Check that month is present in the list
    def test_month_in_list(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        for month in months:
            with self.subTest(month=month):
                self.assertIn(month, months)

if __name__ == "__main__":
    unittest.main()
