import math
import unittest

from measurement import to_millimeters


class MeasurementTests(unittest.TestCase):
    def test_conversion_factors(self):
        for unit, expected in (
            ("mm", 2.0), ("cm", 20.0), ("m", 2000.0),
            ("in", 50.8), ("ft", 609.6),
        ):
            with self.subTest(unit=unit):
                result = to_millimeters(2, unit)
                self.assertIsInstance(result, float)
                self.assertAlmostEqual(result, expected)

    def test_fraction_and_normalized_unit(self):
        self.assertAlmostEqual(to_millimeters(0.5, " IN "), 12.7)

    def test_zero(self):
        self.assertEqual(to_millimeters(0, "ft"), 0.0)

    def test_invalid_values(self):
        for value in (-1, True, False, math.nan, math.inf, -math.inf, "2", None):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    to_millimeters(value, "mm")

    def test_invalid_units(self):
        for unit in ("yard", "", None, 12):
            with self.subTest(unit=unit):
                with self.assertRaises(ValueError):
                    to_millimeters(2, unit)


if __name__ == "__main__":
    unittest.main()
