from datetime import date
def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""
    def withdraw(amount):
     #   nonlocal balance
     #   balance = balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw
def demo(balance):
    def bigger(amount):
        if amount > balance:
            amount += 1
        return balance
    return bigger