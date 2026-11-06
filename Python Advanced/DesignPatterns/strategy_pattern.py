class PaymentStrategy:

    def pay(self):

        pass


class CashPayment(

    PaymentStrategy

):

    def pay(self):

        print("Cash Payment")


class CardPayment(

    PaymentStrategy

):

    def pay(self):

        print("Card Payment")


payment = CardPayment()

payment.pay()