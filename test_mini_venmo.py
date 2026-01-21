import unittest
from mini_venmo import MiniVenmo
from user import User

class TestMiniVenmo(unittest.TestCase):
    def setUp(self):
        self.venmo = MiniVenmo()

    def test_create_user(self):
        user = self.venmo.create_user("Carol", 20.0, "4111111111111111")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "Carol")
        self.assertEqual(user.balance, 20.0)
        self.assertEqual(user.credit_card_number, "4111111111111111")

    def test_create_user_invalid_card(self):
        with self.assertRaises(Exception):
            self.venmo.create_user("Bob123", 10.0, "0000000000000000")

    def test_payment_with_balance(self):
        carol = self.venmo.create_user("Carol", 20.0, "4111111111111111")
        bob = self.venmo.create_user("Bobby", 10.0, "4242424242424242")
        payment = carol.pay(bob, 5.0, "Coffee")
        self.assertEqual(carol.balance, 15.0)
        self.assertEqual(bob.balance, 15.0)
        self.assertEqual(payment.amount, 5.0)
        self.assertEqual(payment.note, "Coffee")

    def test_payment_with_card(self):
        carol = self.venmo.create_user("Carol", 2.0, "4111111111111111")
        bob = self.venmo.create_user("Bobby", 10.0, "4242424242424242")
        payment = carol.pay(bob, 5.0, "Lunch")
        self.assertEqual(carol.balance, 2.0)
        self.assertEqual(bob.balance, 15.0)
        self.assertEqual(payment.amount, 5.0)
        self.assertEqual(payment.note, "Lunch")

    def test_render_feed(self):
        carol = self.venmo.create_user("Carol", 20.0, "4111111111111111")
        bob = self.venmo.create_user("Bobby", 10.0, "4242424242424242")
        bob.pay(carol, 5.0, "Coffee")
        feed = bob.retrieve_feed()
        self.venmo.render_feed(feed)
        self.assertEqual(self.venmo.render_feed(feed), "Bobby paid Carol $5.0 for Coffee")

if __name__ == '__main__':
    unittest.main()