from admin import Admin

# Example usage:
admin = Admin()

# Create user accounts
user1 = admin.create_account("John Doe", "john@example.com", "123 Main St", "Savings")
user2 = admin.create_account("Jane Smith", "jane@example.com", "456 Elm St", "Current")

# Deposit and withdraw
print(user1.deposit(1000))
print(user2.withdraw(500))

# Check balance and transaction history
print(user1.check_balance())
print(user2.check_transaction_history())

# Take a loan
print(user1.take_loan(500))
print(user1.take_loan(200))
print(user1.take_loan(100))

# Transfer money
print(user1.transfer(user2, 300))
print(user2.transfer(user1, 200))

# Admin operations
print(admin.list_accounts())
print(admin.total_balance())
print(admin.total_loan_amount())
print(admin.toggle_loan_feature(False))
