try:
    result = 10 / 0  # This will cause an error
except Exception as e:
    with open("error_log.txt", "a") as file:
        file.write(f"Error: {str(e)}\n")

# Check error_log.txt for errors
