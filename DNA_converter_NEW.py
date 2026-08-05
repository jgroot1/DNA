# ask the user if they want to import their DNA from a file or the consol
from utils.input_type_chose import file_input_function
input_from_file = file_input_function()

# ask the user if they want the program to automatically remove invalid characters from the DNA
from utils.remove_error_chose import invalid_removal_choice_function
remove_errors = invalid_removal_choice_function()

#input for the DNA from the file or the consol
from utils.DNA_input import input_file_consol_function
DNA = input_file_consol_function(input_from_file)

#everything for handling errors in the DNA
from utils.error_removal import remove_errors_function
DNA = remove_errors_function(DNA, remove_errors, input_from_file)