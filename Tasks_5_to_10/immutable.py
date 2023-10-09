from cryptography.fernet import Fernet
class Customer:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self._balance = 0  # Encapsulate balance as a private attribute
    def get_balance(self):
        # Implement access control logic here
        if not self.is_authorized():
            raise PermissionError("Access denied to balance.")
        return self._balance
    def is_authorized(self):
        if self.name in ["sowji", "sowjanya"]:
            return True
        else:
            return False
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data
# Input customer details
customer_name = input("Enter Customer Name: ").title().lower()
customer_account_number = input("Enter Customer Account Number: ")
initial_balance = float(input("Enter Initial Balance: "))

# Create a customer instance
customer = Customer(customer_name, customer_account_number)

# Print initial customer details
print(f"Customer Name: {customer.name}")
print(f"Account Number: {customer.account_number}")
print(f"Initial Balance: {initial_balance}")

# Simulate a balance update (for demonstration purposes)
if customer.is_authorized():
    transfer_amount = float(input("Enter Transfer Amount: "))
    if transfer_amount <= initial_balance:
        initial_balance -= transfer_amount
        print("Transfer successful.")
    else:
        print("Insufficient balance for the transfer.")
else:
    print("Authorization denied for the transfer.")

# Encrypt and decrypt sensitive data (for demonstration purposes)
encryption_key = Fernet.generate_key()
sensitive_data = "Sensitive customer data"
encrypted_data = encrypt_data(sensitive_data, encryption_key)
decrypted_data = decrypt_data(encrypted_data, encryption_key)

print(f"Sensitive Data: {sensitive_data}")
print(f"Encrypted Data: {encrypted_data}")
print(f"Decrypted Data: {decrypted_data}")


# class Customer:
#     def __init__(self, name, account_number):
#         self.name = name
#         self.account_number = account_number
#         self._balance = 0  # Encapsulate balance as a private attribute
#         self._transactions = []  # Use a list for mutable transactions
#
#     def get_balance(self):
#         # Implement access control logic here
#         if not self.is_authorized():
#             raise PermissionError("Access denied to balance.")
#         return self._balance
#
#     def is_authorized(self):
#         if self.name in ["sowji", "sowjanya"]:
#             return True
#         else:
#             return False
#
#     def add_transaction(self, amount):
#         # Add transactions to the list
#         self._transactions.append(amount)
#
#     def get_transactions(self):
#         return tuple(self._transactions)  # Return a tuple for immutable transactions
#
# # Input customer details
# customer_name = input("Enter Customer Name: ").title().lower()
# customer_account_number = input("Enter Customer Account Number: ")
# initial_balance = float(input("Enter Initial Balance: "))
#
# # Create a customer instance
# customer = Customer(customer_name, customer_account_number)
#
# # Print initial customer details
# print(f"Customer Name: {customer.name}")
# print(f"Account Number: {customer.account_number}")
# print(f"Initial Balance: {initial_balance}")
#
# # Simulate a balance update (for demonstration purposes)
# if customer.is_authorized():
#     transfer_amount = float(input("Enter Transfer Amount: "))
#     if transfer_amount <= initial_balance:
#         initial_balance -= transfer_amount
#         customer.add_transaction(transfer_amount)  # Add the transaction
#         print("Transfer successful.")
#     else:
#         print("Insufficient balance for the transfer.")
# else:
#     print("Authorization denied for the transfer.")
#
# # Access and display transactions as a tuple (immutable)
# transactions = customer.get_transactions()
# print(f"Transactions: {transactions}")
#
# # Access and display balance
# balance = customer.get_balance()
# print(f"Balance: {balance}")




# # Input user details
# user_Id = input("Enter User ID: ")
# user_name = input("Enter User Name: ").title()
# amount = int(input("Enter Total amount: "))
#
# # Create a user_details tuple
# user_details = (user_Id, user_name, amount)
# print(f"Initial amount: {user_details}")
#
# # Define a function to perform amount transfer
# def amount_transfer(args):
#     user_list = list(args)
#     for i in range(len(user_list)):
#         if type(user_list[i]) == int:
#             tnsf = int(input("Enter transfer amount: "))
#             if amount > tnsf:
#                 user_list[i] = user_list[i] - tnsf
#     return tuple(user_list)
#
# # Call the function and update user_details
# user_details = amount_transfer(user_details)
# print(f"Updated amount: {user_details}")
