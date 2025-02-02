# Writing to a file
with open("user.txt", "w") as file:
    file.write("Alice\n")

# Reading from the file
with open("user.txt", "r") as file:
    print(file.read())  # Output: Alice
