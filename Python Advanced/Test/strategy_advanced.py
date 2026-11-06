class CreditCard:

    def pay(self):

        print(
            "Credit Card Payment"
        )


class PayPal:

    def pay(self):

        print(
            "PayPal Payment"
        )


class PaymentContext:

    def __init__(
        self,
        strategy
    ):
        self.strategy = strategy

    def execute(self):

        self.strategy.pay()


payment = PaymentContext(
    PayPal()
)

payment.execute()