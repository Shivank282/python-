# Writing to source file
with open("source.txt", "w") as file:
    file.write("This is a copied file content.")

# Copying content
with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    dest.write(src.read())

# Verifying copied content
with open("destination.txt", "r") as file:
    print(file.read())  # Output: This is a copied file content.
