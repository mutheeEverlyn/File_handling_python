#a program that reads a file and writes a modified version to a new file.

def read_and_modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        modified_content = content.upper()  # change the content to uppercase
        
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Content from {input_file} has been modified and written to {output_file}.")
    
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file = 'input.txt'
output_file = 'output.txt'
read_and_modify_file(input_file, output_file)
