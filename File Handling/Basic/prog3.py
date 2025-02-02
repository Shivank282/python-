with open("notes.txt", "a") as file:
    while True:
        line = input("Enter text (type 'exit' to stop): ")
        if line.lower() == "exit":
            break
        file.write(line + "\n")

# Reading the file
with open("notes.txt", "r") as file:
    print(file.read())
