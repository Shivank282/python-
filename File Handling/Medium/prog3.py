# Writing sample text
with open("replace.txt", "w") as file:
    file.write("Hello world, Python is amazing.")

# Replacing 'Python' with 'Programming'
with open("replace.txt", "r") as file:
    content = file.read().replace("Python", "Programming")

# Writing updated content back to file
with open("replace.txt", "w") as file:
    file.write(content)

# Verifying changes
with open("replace.txt", "r") as file:
    print(file.read())  # Output: Hello world, Programming is amazing.
