# Ask the user for a filename and handle errors
filename = input("Enter the name of the file to read: ")

try:
    # Attempt to open the file
    with open(filename, "r") as file:
        # Read and display its content
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"The file '{filename}' does not exist. Please check the filename and try again.")
except PermissionError:
    print(f"You do not have permission to access the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
