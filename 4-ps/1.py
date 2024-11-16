# Initialize an empty list to store fruit names
fruits = []

# Ask the user to input the names of seven fruits
for i in range(7):
    fruit = input(f"Enter the name of fruit {i + 1}: ")
    fruits.append(fruit)

# Display the list of fruits
print("\nThe list of fruits you entered is:")
print(fruits)
