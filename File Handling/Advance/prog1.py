# Writing to a CSV file
with open("data.csv", "w") as file:
    file.write("Name,Age,City\nAlice,25,New York\nBob,30,Los Angeles\n")

# Reading CSV file and displaying structured data
with open("data.csv", "r") as file:
    for line in file:
        print(line.strip().split(","))

# Output:
# ['Name', 'Age', 'City']
# ['Alice', '25', 'New York']
# ['Bob', '30', 'Los Angeles']
