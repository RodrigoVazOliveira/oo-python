from account import Account


def create_account(number, holder, balance, limit):
    """

    :rtype: object
    """
    account = Account(number, holder, balance, limit)

    return account
