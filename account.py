import json


class Account:
    def __init__(self, number, holder, balance, limit):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def statement(self):
        print("O saldo atual e de R$ {}".format(self.balance))

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

