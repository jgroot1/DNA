# ask the user if they want to import their DNA from a file or the consol
from utils.file_input import file_input
input_from_file = file_input()

# ask the user if they want the program to automatically remove invalid characters from the DNA
from utils.remove_error import remove_invalid_verify_input
remove_errors = remove_invalid_verify_input()