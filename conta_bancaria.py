from account import Account


def create_account(number, holder, balance, limit):
    account = Account(number, holder, balance, limit)

    return account


def deposit(account, value):
    account.balance += value


def withdraw(account, value):
    account.balance -= value


def statement(account):
    print("O saldo atual e R$ {}".format(account.balance))
