class Employee:
    def __init__(self, emp_id, name, email):
        self.emp_id = emp_id
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


class Manager(Employee):
    def __init__(self, emp_id, name, email, team_size):
        super().__init__(emp_id, name, email)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")

    def manage_team(self):
        print(f"{self.name} is managing a team of {self.team_size} developers.")


class Developer(Employee):
    def __init__(self, emp_id, name, email, programming_language):
        super().__init__(emp_id, name, email)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")

# Function to get user input with error handling
def get_user_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

# Example usage with user input and exception handling:
if __name__ == "__main__":
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    employee = Employee(emp_id, name, email)
    employee.display_info()

    emp_id = input("Enter Manager's Employee ID: ")
    name = input("Enter Manager's Name: ")
    email = input("Enter Manager's Email: ")
    team_size = get_user_input("Enter Manager's Team Size: ", int)
    manager = Manager(emp_id, name, email, team_size)
    manager.display_info()
    manager.manage_team()

    emp_id = input("Enter Developer's Employee ID: ")
    name = input("Enter Developer's Name: ")
    email = input("Enter Developer's Email: ")
    programming_language = input("Enter Developer's Programming Language: ")
    developer = Developer(emp_id, name, email, programming_language)
    developer.display_info()
    developer.write_code()
