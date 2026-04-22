# bank.py

# Import BankAccount from bank_account.py (if you keep it in the same folder)
try:
    from bank_account import BankAccount
except ImportError:
    # Or copy the BankAccount class here for now
    class BankAccount:
        def __init__(self, initial_balance=0.0):
            self._balance = initial_balance

        @property
        def balance(self):
            return self._balance

        @balance.setter
        def balance(self, value):
            if value < 0:
                raise ValueError("Balance cannot be negative")
            self._balance = value

        def __str__(self):
            return f"BankAccount: £{self.balance:.2f}"

        def deposit(self, amount):
            self._balance += amount

        def withdraw(self, amount):
            self._balance -= amount


class Bank:
    def __init__(self, name):
        # TODO: store name
        self.name = name
        # TODO: store a list of accounts (composition)
        self._accounts = []

    def add_account(self, account):
        # TODO: add account to self._accounts
        # Maybe check type: isinstance(account, BankAccount)
        self._accounts.append(account)

    def total_balance(self):
        # TODO: sum balance of all accounts
        return sum(account.balance for account in self._accounts)

    def find_account(self, name):
        # TODO: return first BankAccount whose __str__ or name matches (you can extend BankAccount later)
        for account in self._accounts:
            if str(account).find(name) != -1:
                return account
        return None

    def __str__(self):
        # TODO: human‑readable string
        # e.g. "Bank(name='Tesco Bank') with 3 accounts"
        count = len(self._accounts)
        return f"Bank(name={self.name!r}) with {count} accounts"


# --- Testing code ---
if __name__ == "__main__":
    bank = Bank("Tesco Bank")

    # Create some accounts
    a1 = BankAccount(100.0)
    a2 = BankAccount(200.0)
    a3 = BankAccount(300.0)

    # Add them to the bank
    bank.add_account(a1)
    bank.add_account(a2)
    bank.add_account(a3)

    print("Bank:", bank)
    print("Total balance:", bank.total_balance())

    # Find account (simple search)
    found = bank.find_account("BankAccount: £100.00")
    if found:
        print("Found:", found)
    else:
        print("Account not found.")

    # Deposit to first account
    a1.deposit(50.0)
    print("After depositing 50 to first account...")
    print("Total balance:", bank.total_balance())
    #ex 2
    a1.deposit(-50.0)
    print("After depositing 50 to first account...")
    print("Total balance:", bank.total_balance())