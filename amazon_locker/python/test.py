import unittest
from datetime import datetime, timedelta

from locker import Locker
from compartment import Compartment
from size import Size

num_small = 1
num_medium = 1
num_large = 1

class TestLocker(unittest.TestCase):
    def setUp(self):
        self.locker = Locker()

        for _ in range(num_small):
            self.locker.compartments.append(Compartment(Size.SMALL))
        
        for _ in range(num_medium):
            self.locker.compartments.append(Compartment(Size.MEDIUM))
        
        for _ in range(num_large):
            self.locker.compartments.append(Compartment(Size.LARGE))


    def test_deposit_and_pickup(self):
        code = self.locker.deposit_package(Size.SMALL)

        self.assertEqual(code, "0")
        self.assertIn(code, self.locker.access_tokens)

        comp = self.locker.access_tokens[code].get_compartment()
        self.assertEqual(comp.get_size(), Size.SMALL)
        self.assertTrue(comp.is_occupied())
        
        self.locker.pickup(code)

        self.assertFalse(comp.is_occupied())
        self.assertNotIn(code, self.locker.access_tokens)

    def test_full_compartment_rejects_deposit(self):
        code = self.locker.deposit_package(Size.SMALL)

        with self.assertRaisesRegex(RuntimeError, "No available compartment"):
            self.locker.deposit_package(Size.SMALL)

        self.assertEqual(len(self.locker.access_tokens), 1)
        self.assertTrue(self.locker.access_tokens[code].get_compartment().is_occupied())

    def test_invalid_code_rejects_pickup(self):
        code = self.locker.deposit_package(Size.SMALL)

        with self.assertRaisesRegex(ValueError, "Invalid token code"):
            self.locker.pickup("invalid")

        self.assertIn(code, self.locker.access_tokens)
        self.assertTrue(self.locker.access_tokens[code].get_compartment().is_occupied())

    def test_expired_token_rejects_pickup(self):
        code = self.locker.deposit_package(Size.SMALL)
        token = self.locker.access_tokens[code]
        token.expiration = datetime.now() - timedelta(days=1)

        with self.assertRaisesRegex(ValueError, "Token expired"):
            self.locker.pickup(code)

        self.assertIn(code, self.locker.access_tokens)
        self.assertTrue(token.get_compartment().is_occupied())

    def test_multiple_deposits_generate_distinct_codes(self):
        small_code = self.locker.deposit_package(Size.SMALL)
        medium_code = self.locker.deposit_package(Size.MEDIUM)

        self.assertNotEqual(small_code, medium_code)
        self.assertEqual(len(self.locker.access_tokens), 2)
        self.assertEqual(
            self.locker.access_tokens[small_code].get_compartment().get_size(),
            Size.SMALL,
        )
        self.assertEqual(
            self.locker.access_tokens[medium_code].get_compartment().get_size(),
            Size.MEDIUM,
        )

    def test_pickup_makes_compartment_available_again(self):
        first_code = self.locker.deposit_package(Size.SMALL)
        comp = self.locker.access_tokens[first_code].get_compartment()
        self.locker.pickup(first_code)

        second_code = self.locker.deposit_package(Size.SMALL)

        self.assertNotEqual(first_code, second_code)
        self.assertIs(self.locker.access_tokens[second_code].get_compartment(), comp)
        self.assertTrue(comp.is_occupied())
        self.assertNotIn(first_code, self.locker.access_tokens)


if __name__ == "__main__":
    unittest.main()
