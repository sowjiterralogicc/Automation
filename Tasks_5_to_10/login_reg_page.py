# Simulated user database (in practice, you would use a real database)
users = {
    'sowji': {'password': 'Ammu1998@17', 'role': 'user'},
    'sowji1': {'password': 'Sowji1998@17', 'role': 'admin'},
}

# Simulated session (in practice, use a secure session management system)
current_user = None    #indicates that no user is authenticated

# Decorator to check if a user is authenticated
def login_required(func):
    def wrapper(*args, **kwargs):
        global current_user
        if current_user is None:
            print("Authentication required. Please log in.")
        else:
            return func(*args, **kwargs)
    return wrapper

# Decorator to check if a user has the required role
def role_required(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            global current_user
            if current_user is None:
                print("Authentication required. Please log in.")
            elif users[current_user]['role'] != required_role:
                print(f"Access denied. This operation requires '{required_role}' role.")
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

# Function for user registration
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        print("Username already exists. Please choose a different one.")
    else:
        role = input("Enter user role (user/admin): ").lower()
        if role not in ['user', 'admin']:
            print("Invalid role. Allowed roles are 'user' and 'admin'.")
        else:
            users[username] = {'password': password, 'role': role}
            print("Registration successful. Please log in.")

# Function for user login
def login():
    global current_user
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password:
        current_user = username
        print("Login successful!")
    else:
        print("Login failed. Check your username and password.")

# Function for a protected operation for users
@role_required('user')
def user_operation():
    print(f"User operation performed by {current_user}.")

# Function for a protected operation for admins
@role_required('admin')
def admin_operation():
    print(f"Admin operation performed by {current_user}.")

# Main loop for user interaction
while True:
    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. Perform User Operation")
    print("4. Perform Admin Operation")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        user_operation()
    elif choice == '4':
        admin_operation()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")