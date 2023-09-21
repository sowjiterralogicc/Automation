import random
import string

class UsernameGenerator:
    def __init__(self, username_length=8):
        self.username_length = username_length
        self.used_usernames = set()
        self.total_possible_usernames = len(string.ascii_letters + string.digits) ** username_length
        self.generated_usernames_count = 0

    def generate_username(self):
        while self.generated_usernames_count < self.total_possible_usernames:
            # Generate a random username
            first_letter = random.choice(string.ascii_uppercase)
            print("first_letter::::::",first_letter)
            rest_of_username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=self.username_length - 1))
            print("self.username_length::::::",self.username_length)
            print("Rest of username:::::::::",rest_of_username)
            username = first_letter + rest_of_username

            # Check if the username is unique
            if username not in self.used_usernames:
                self.used_usernames.add(username)
                self.generated_usernames_count += 1
                yield username
        yield None  # Signal that no more unique usernames can be generated

# Example usage:
if __name__ == "__main__":
    generator = UsernameGenerator(username_length=8)

    # Generate and print 10 unique usernames
    for i in range(10):
        username = next(generator.generate_username())
        if username is not None:
            print(f"Generated Username {i + 1}: {username}")
        else:
            print("No more unique usernames can be generated.")
            break
