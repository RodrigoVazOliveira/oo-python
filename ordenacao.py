from typing import List


class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


print(Conta(88))


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()  # duck typing


from functools import total_ordering


@total_ordering
class AccountSalary:

    def __init__(self, code, balance):
        self._code = code
        self._balance = balance

    def deposit(self, value):
        self._balance += value

    def __str__(self) -> str:
        return f"[>>> Código: {self._code}, Salário: {self._balance} <<<<]"

    def __eq__(self, o) -> bool:
        if type(o) != AccountSalary:
            return False
        return self._code == o._code

    def __lt__(self, other):
        if self._balance != other._balance:
            return self._balance < other._balance
        return self._code < other._code





account_salary_one = AccountSalary(1, 42.00)
account_salary_two = AccountSalary(1, 53.00)

print(account_salary_one)
print(account_salary_two)
print("Conta um e menor que a cont do dois {}".format(account_salary_one < account_salary_two))
print("Conta um e maior que a cont do dois {}".format(account_salary_one > account_salary_two))
print("Conta um e menor ou igual que a cont do dois {}".format(account_salary_one <= account_salary_two))
print("Conta um e maior ou igual que a cont do dois {}".format(account_salary_one >= account_salary_two))


print(account_salary_one == account_salary_two)

ages = [15, 87, 65, 57, 32, 49, 37]

for i in range(len(ages)):
    print(i, ages[i])

ages_enumerate = list(enumerate(ages))
print(ages_enumerate)

for index, value in ages_enumerate:
    print(f"indice: {index}, idade: {value}")

users = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

print("Usuario")
for _, age, _ in users:
    print(f"idade: {age}")

ages_orded_natural: list[int] = sorted(ages)
ages_orded_reverse = sorted(ages, reverse=True)  # pode usar list(reversed(ages))

print(ages_orded_natural)
print(ages_orded_reverse)

# já com a própria lista
ages.sort()
print(f"Lista de idades ordenadas: {ages}")
ages.reverse()
print(f"Lista de idades revertidas: {ages}")
