import re

from exceptions import UsernameException, CreditCardException, PaymentException
from feed import Feed
from payment import Payment

class User:

    def __init__(self, username):
        self.credit_card_number = None
        self.balance = 0.0
        self.feed = Feed(self)
        self.friends = []

        if self._is_valid_username(username):
            self.username = username
        else:
            raise UsernameException('Username not valid.')

    def retrieve_feed(self):
        return self.feed

    def add_friend(self, new_friend):
        self.friends.append(new_friend)

    def add_to_balance(self, amount):
        self.balance += float(amount)

    def add_credit_card(self, credit_card_number):
        if self.credit_card_number is not None:
            raise CreditCardException('Only one credit card per user!')

        if self._is_valid_credit_card(credit_card_number):
            self.credit_card_number = credit_card_number

        else:
            raise CreditCardException('Invalid credit card number.')

    def pay(self, target, amount, note):
        amount = float(amount)
        payment = self.pay_with_balance(target,amount, note) if (
            self.balance >= amount) else self.pay_with_card(target, amount, note)
        self._add_payment_to_feed(payment)
        return payment

    def pay_with_card(self, target, amount, note):
        amount = float(amount)

        self.common_payment_validations(target, amount)
        if (self.credit_card_number is None):
            raise PaymentException('Must have a credit card to make a payment.')

        self._charge_credit_card(self.credit_card_number)
        payment = Payment(amount, self, target, note)
        target.add_to_balance(amount)

        return payment

    def pay_with_balance(self, target, amount, note):
        amount = float(amount)
        self.common_payment_validations(target, amount)

        self.balance -= amount

        payment = Payment(amount, self, target, note)
        target.add_to_balance(amount)

        return payment

    def common_payment_validations(self, target, amount):
        if (self.username == target.username):
            raise PaymentException('User cannot pay themselves.')
        elif (amount <= 0.0):
            raise PaymentException('Amount must be a non-negative number.')
        return

    def _add_payment_to_feed(self, payment):
        self.feed.payments.append(payment)

    def _is_valid_credit_card(self, credit_card_number):
        return credit_card_number in ["4111111111111111", "4242424242424242"]

    def _is_valid_username(self, username):
        return re.match('^[A-Za-z0-9_\\-]{4,15}$', username)

    def _charge_credit_card(self, credit_card_number):
        # magic method that charges a credit card thru the card processor
        pass