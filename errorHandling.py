def error_handling():
    try:
        # Ask user for filename
        filename = input("Enter the filename to read: ")

        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        print("\nFile content:")
        print(content)

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


error_handling()
