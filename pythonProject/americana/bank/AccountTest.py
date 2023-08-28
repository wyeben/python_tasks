import unittest

from americana.bank.Account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("1", 1)

    def test_initial_balance(self):
        self.assertEqual(0.0, self.account.get_balance())

    def test_can_deposit_money(self):
        self.account.deposit(1000.0)
        self.assertEqual(1000.0, self.account.get_balance())

    def test_can_withdraw_sufficient_funds(self):
        self.account.deposit(2000.0)
        self.assertTrue(self.account.withdraw(1000.0, 1))
        self.assertEqual(1000.0, self.account.get_balance())

    def test_cannot_withdraw_insufficient_funds(self):
        self.account.deposit(500.0)
        self.assertFalse(self.account.withdraw(1000.0, 1))
        self.assertEqual(500.0, self.account.get_balance())

    def test_cannot_withdraw_with_incorrect_pin(self):
        self.account.deposit(2000.0)
        self.assertFalse(self.account.withdraw(1000.0, 3))
        self.assertEqual(2000.0, self.account.get_balance())

    def test_check_account_number(self):
        self.assertEqual("1", self.account.get_account_number())

    def test_register_an_account(self):
        self.account.register("Yila", "Benson")
        self.account.set_account_number("12243645")
        self.assertEqual("Yila Benson - 12243645",  self.account.get_account_details())

