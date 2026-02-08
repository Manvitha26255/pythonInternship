class Payment:
    def pay(self):
        print("Payment is being processed")

class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay")

class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")

class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")

p = Payment()
g = GooglePay()
ph = PhonePe()
c = CreditCard()

p.pay()
g.pay()
ph.pay()
c.pay()
