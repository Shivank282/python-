# Writing sample text to a file
with open("words.txt", "w") as file:
    file.write("Python is great for file handling.\n")

# Counting words
with open("words.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())

print("Total words:", word_count)  # Output: Total words: 5
