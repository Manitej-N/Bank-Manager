# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        # TODO: store initial_balance as a private attribute
        # Use naming convention: self._balance
        self._balance = initial_balance

    @property
    def balance(self):
        # TODO: return self._balance (read‑only like view)
        return self._balance

    @balance.setter
    def balance(self, value):
        # TODO:
        # - raise ValueError if value < 0
        # - otherwise set self._balance = value
        if value < 0:
            raise ValueError("Balance cannot be negative")
        else:
            self._balance = value

    def __str__(self):
        # TODO: human‑readable string
        # e.g. "BankAccount: £100.00"
        return f"BankAccount: £{self.balance:.2f}"

    def deposit(self, amount):
        # TODO: add amount to balance (no extra checks; use property setter)
        self._balance += amount

    def withdraw(self, amount):
        # TODO: subtract amount from balance
        # Let the setter handle negative balance logic
        self._balance -= amount


# --- Testing code ---
if __name__ == "__main__":
    account = BankAccount(100.0)

    print("Initial:", account)

    account.deposit(50.0)
    print("After deposit 50:", account)

    account.withdraw(30.0)
    print("After withdraw 30:", account)

    # This should raise an error (or clamp to 0, your choice)
    try:
        print("\nTrying to set balance to -50...")
        account.balance = -50.0
    except ValueError as e:
        print("Error:", e)

    print("\nFinal state:", account)