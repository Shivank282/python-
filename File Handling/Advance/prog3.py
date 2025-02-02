# Creating two sample files
with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("Content of file 1.\n")
    f2.write("Content of file 2.\n")

# Merging files
with open("merged.txt", "w") as merged:
    for filename in ["file1.txt", "file2.txt"]:
        with open(filename, "r") as file:
            merged.write(file.read() + "\n")

# Verifying merged content
with open("merged.txt", "r") as file:
    print(file.read())

# Output:
# Content of file 1.
# Content of file 2.
