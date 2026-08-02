# ask the user if they want to import their DNA from a file or the consol
from utils.input_type_chose import file_input
input_from_file = file_input()

# ask the user if they want the program to automatically remove invalid characters from the DNA
from utils.remove_error_chose import remove_invalid
remove_errors = remove_invalid()

from utils.DNA_input import input_file_consol
DNA = input_file_consol(input_from_file)

if remove_errors:
    from utils.error_removal import remove_errors
    DNA = remove_errors(DNA)