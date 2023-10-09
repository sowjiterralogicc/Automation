# class StudentManager:
#     def __init__(self):
#         self.students = []
#     def add_student(self, name, age):
#         student = {"name": name, "age": age}
#         self.students.append(student)
#     def get_students(self):
#         return self.students.copy()
#     def update_student_age(self, index, new_age):
#         if 0 <= index < len(self.students):
#             print("index:::::",index)
#             print("len(self.students:::::::::",len(self.students))
#             self.students[index]["age"] = new_age
#         else:
#             raise IndexError("Index out of range. No student found at the specified index.")
# def main():
#     student_manager = StudentManager()
#     try:
#         # Add students
#         student_manager.add_student("Alice", 20)
#         student_manager.add_student("Bob", 21)
#         student_manager.add_student("Charlie", 22)
#         student_manager.add_student("Charlie", 22)
#         # Get a copy of the student list
#         students_copy = student_manager.get_students()
#         # Modify the age of the first student in the copied list
#         student_manager.update_student_age(3, 30)
#         # Print the first student in the copied list
#         print(students_copy)
#         print(type(students_copy))
#         # Print the list of students from the student manager (original list)
#         print(student_manager.get_students())
#     except IndexError as e:
#         print(f"Error: {e}")
# if __name__ == "__main__":
#     main()

#A shallow copy creates a new container (e.g., a new list)
# but does not create new copies of the elements within the container.
# Instead, it copies references to the original elements.


# import copy
# class ConfigurationManager:
#     def __init__(self, config):
#         self.config = config
#
#     def get_production_config(self):
#         return self.config
#
#     def get_test_config(self):
#         return copy.deepcopy(self.config)
#
#     def modify_test_config(self, server_port=None, db_name=None, db_username=None, db_password=None):
#         if "server" in self.config:
#             if server_port is not None:
#                 self.config["server"]["port"] = server_port
#
#         if "database" in self.config:
#             if db_name is not None:
#                 self.config["database"]["name"] = db_name
#             if db_username is not None:
#                 self.config["database"]["username"] = db_username
#             if db_password is not None:
#                 self.config["database"]["password"] = db_password
#
# def main():
#     production_config = {
#         "server": {
#             "host": "google.com",
#             "port": 8080
#         },
#         "database": {
#             "name": "mysql",
#             "username": "root",
#             "password": "root"
#         }
#     }
#
#     config_manager = ConfigurationManager(production_config)
#
#     try:
#         test_config = config_manager.get_test_config()
#
#         # Modify the test configuration
#         config_manager.modify_test_config(server_port=9090, db_name="test_db", db_username="test_user", db_password="test_password")
#
#         # Print the production and test configurations
#         print("Production Configuration:")
#         print(production_config)
#
#         print("\nTest Configuration:")
#         print(test_config)
#     except KeyError as e:
#         print(f"Error: Configuration key not found - {e}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# if __name__ == "__main__":
#     main()


#A deep copy creates a completely independent copy of the container and all of its elements, recursively.
# This ensures that changes made to the copied container or its elements won't affect the original.


#
# import copy
# d = [1, 2, 3, 4]
# d1 = copy.copy(d)
# print(id(d1),id(d))
# d1[1] = 40
# print("d1:::", d1)
# print(d)

# import copy
# l=[1,[2,3],4]
# l1=copy.copy(l)
# l1[1][0]=30
# print(id(l1[0]),id(l[0]))
# print("l1::::",l1)
# print("l::::",l)

# import copy
#
# original_list = [1, 2, 3, 4]
# shallow_copied_list = copy.copy(original_list)
#
# # Modifying the copied list affects the original list
# shallow_copied_list[1] = 40
# print(shallow_copied_list)
# print(original_list)  # Output: [1, 40, 3, 4]



# import copy
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # Create an original Person object
# person1 = Person("John Doe", 30)
#
# # Create a shallow copy of the Person object
# person2 = copy.copy(person1)
#
# # Print the names and ages of both objects
# print(person1.name, person1.age)
# print(person2.name, person2.age)

# class ShallowCopy:
#     def __init__(self, list_of_dicts):
#         self.list_of_dicts = list_of_dicts
#
#     def create_shallow_copy(self):
#         shallow_copy = []
#         for d in self.list_of_dicts:
#             shallow_copy.append(dict(d))
#         return shallow_copy
# def create_shallow_copy(list_of_dicts):
#     return ShallowCopy(list_of_dicts).create_shallow_copy()
#
#
# def main():
#     list_of_dicts = [{'name': 'Alice', 'age': 23}, {'name': 'Bob', 'age': 19}]
#
#     # Create a shallow copy
#     shallow_copy = create_shallow_copy(list_of_dicts)
#
#     # Modify the shallow copy
#     print("id of lists::::",id(list_of_dicts[0]["age"]),id(shallow_copy[0]["age"]))
#     shallow_copy[0]["age"] = 24
#
#     # Print the original and shallow copy
#     print("Original:")
#     print(list_of_dicts)
#     print(list_of_dicts[0]["age"])
#     print("Shallow copy:")
#     print(shallow_copy)
#     print(shallow_copy[0]["age"])
#
#
# if __name__ == "__main__":
#     main()
#
import copy
# l= [1,[2,3],4]
# shallow_copy = copy.copy(l)
# print(l)
# print(shallow_copy)
# l.append([4,5,6])
# print(l)
# print(shallow_copy)
l = [1,2,3,4]
deep_copy = copy.deepcopy(l)
l[0] = 200
print(l)
print(deep_copy)












