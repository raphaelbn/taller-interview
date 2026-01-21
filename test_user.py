import unittest
from user import User
from exceptions import UsernameException, CreditCardException

class TestUser(unittest.TestCase):

    def test_valid_username(self):
        user = User("ValidUser")
        self.assertEqual(user.username, "ValidUser")

    def test_invalid_username(self):
        with self.assertRaises(UsernameException):
            User("inv@lid")

    def test_add_credit_card_success(self):
        user = User("TestUser")
        user.add_credit_card("4111111111111111")
        self.assertEqual(user.credit_card_number, "4111111111111111")

    def test_add_credit_card_twice(self):
        user = User("TestUser")
        user.add_credit_card("4111111111111111")
        with self.assertRaises(CreditCardException):
            user.add_credit_card("4242424242424242")

    def test_add_invalid_credit_card(self):
        user = User("TestUser")
        with self.assertRaises(CreditCardException):
            user.add_credit_card("1234567890123456")

if __name__ == '__main__':
    unittest.main()