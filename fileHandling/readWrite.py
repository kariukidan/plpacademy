# Create and write content to "input.txt" for testing
with open("input.txt", "w") as newfile:
    newfile.write("This is my content")

try:
    # Open the input file for reading
    with open("input.txt", "r") as input_file:
        # Read the file content
        content = input_file.read()

    # Modify the content (convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    with open("output.txt", "w") as output_file:
        output_file.write(modified_content)

    print("File has been successfully modified and saved to 'output.txt'.")

except FileNotFoundError:
    print("The input file 'input.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
