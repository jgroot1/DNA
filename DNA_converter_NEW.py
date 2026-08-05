# ask the user if they want to import their DNA from a file or the consol
from utils import codons_table
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

#gives info about the DNA
from utils.DNA_info import DNA_info_function
DNA = DNA_info_function(DNA)

from utils.DNA_codon_converter import DNA_to_codons_function
codons = DNA_to_codons_function(DNA, input_from_file)

from utils.codons_amino_acids_converter import codons_to_amino_acids_function
codons_to_amino_acids_function(codons, input_from_file)