# Step 1: Define your custom exception classes
class NegativeAmountError(Exception):
    """Exception raised when the withdrawal amount is zero or negative."""
    def __init__(self, amount, message="Withdrawal amount must be greater than zero."):
        self.amount = amount
        self.message = message
        super().__init__(self.message)


class InsufficientFundsError(Exception):
    """Exception raised when the withdrawal amount exceeds the balance."""
    def __init__(self, balance, amount, message="Inadequate funds for this transaction."):
        self.balance = balance
        self.amount = amount
        self.message = message
        super().__init__(self.message)


# Step 2: Create the function using 'raise' to trigger conditions
def withdraw_money(balance, amount):
    if amount <= 0:
        raise NegativeAmountError(amount)
    
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    
    # If no exception is raised, process the withdrawal
    new_balance = balance - amount
    print(f"Transaction successful! Withdrew: ${amount}. Remaining balance: ${new_balance}")
    return new_balance


# Step 3: Test your implementation using try-except blocks
test_balance = 500.00
test_amounts = [-50, 600, 200]

for amt in test_amounts:
    print(f"\nAttempting to withdraw: ${amt} (Current Balance: ${test_balance})")
    try:
        test_balance = withdraw_money(test_balance, amt)
    except NegativeAmountError as e:
        print(f"❌ Error [NegativeAmountError]: {e.message} (You entered: ${e.amount})")
    except InsufficientFundsError as e:
        print(f"❌ Error [InsufficientFundsError]: {e.message}")
        print(f"   Available: ${e.balance} | Requested: ${e.amount}")