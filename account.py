import json


class Account:
    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def get_number(self):
        return self.__number

    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        return self.__limit = list

    def statement(self):
        print("O saldo atual e de R$ {}".format(self.__balance))

    def withdraw(self, value):
        self.__balance -= value

    def deposit(self, value):
        self.__balance += value

    def transfer(self, destination, value):
        self.withdraw(value)
        destination.deposit(value)

    def __str__(self) -> str:
        return json.dumps(self.__dict__)
