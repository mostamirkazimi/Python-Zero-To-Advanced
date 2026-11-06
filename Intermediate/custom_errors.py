class BalanceError(Exception):
    pass


balance = 100

withdraw = 200

if withdraw > balance:

    raise BalanceError(
        "موجودی کافی نیست"
    )