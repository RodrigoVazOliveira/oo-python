from conta_bancaria import create_account
from date import Date


def read_new_account():
    number = int(input("Informe o numero da conta bancarioa: "))
    holder = input("Informe o nome do dono da conta bancária: ")
    balance =  float(input("Digite o saldo atual: "))
    limit = float(input("Digite o limite da conta: "))

    return create_account(number, holder, balance, limit)


if __name__ == '__main__':
    accountOne = read_new_account()
    accountTwo = read_new_account()
    print(accountOne, accountTwo, sep="\n")

    accountOne.transfer(accountTwo, 2000.0)

    print(accountOne, accountTwo, sep="\n")

    date = Date(17, 11, 1991)
    date.format_date()