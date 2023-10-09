class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        print(f"{self.name} is described as an animal")

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def nurse_young(self):
        print(f"{self.name} can nurse its young")

    def describe(self):
        print(f"{self.name} is described as a mammal")

class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def can_fly(self):
        print(f"{self.name} can fly")

    def describe(self):
        print(f"{self.name} is described as a bird")

class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def cold_blooded(self):
        print(f"{self.name} is cold-blooded")

    def describe(self):
        print(f"{self.name} is described as a reptile")

def create_animal():
    try:
        category = input("Enter the animal category (Mammal/Bird/Reptile): ").capitalize()
        name = input("Enter the name of the animal: ")
        species = input("Enter the species of the animal: ")

        if category == "Mammal":
            animal = Mammal(name, species)
        elif category == "Bird":
            animal = Bird(name, species)
        elif category == "Reptile":
            animal = Reptile(name, species)
        else:
            raise ValueError("Invalid animal category")

        return animal

    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    animals = []

    while True:
        action = input("Enter 'create' to create a new animal, 'describe' to describe an animal, 'list' to list all animals, or 'exit' to exit: ").lower()

        if action == 'create':
            animal = create_animal()
            if animal:
                animals.append(animal)
                print(f"{animal.name} created.")
        elif action == 'describe':
            if not animals:
                print("No animals to describe. Create an animal first.")
                continue
            animal_name = input("Enter the name of the animal you want to describe: ")
            for animal in animals:
                if animal.name == animal_name:
                    animal.describe()
                    break
            else:
                print(f"No animal with the name '{animal_name}' found.")
        elif action == 'list':
            if not animals:
                print("No animals to list. Create an animal first.")
            else:
                print("List of Animals:")
                for animal in animals:
                    print(f"{animal.name} ({animal.species})")
        elif action == 'exit':
            break
        else:
            print("Invalid command. Please enter 'create', 'describe', 'list', or 'exit'.")
if __name__ == "__main__":
    main()

