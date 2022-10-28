from conta_bancaria import create_account
from date import Date

if __name__ == '__main__':
    number = int(input("Informe o numero da conta bancarioa: "))
    holder = input("Informe o nome do dono da conta bancária: ")
    balance =  float(input("Digite o saldo atual: "))
    limit = float(input("Digite o limite da conta: "))

    account = create_account(number, holder, balance, limit)
    print(account)

    date = Date(17, 11, 1991)
    date.format_date()