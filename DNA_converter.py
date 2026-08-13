from utils.input_type_chose import file_input_function
from utils.remove_error_chose import invalid_removal_choice_function
from utils.DNA_input import input_file_consol_function
from utils.error_removal import remove_errors_function
from utils.DNA_info import DNA_info_function
from utils.start_stop_reader_choice import start_stop_reader_choice
from utils.DNA_codon_converter import DNA_to_codons_function
from utils.codons_table import codon_table_single, codon_table_short, codon_table_full
from utils.codons_amino_acids_converter import codons_to_amino_acids_function

# ask the user if they want to import their DNA from a file or the consol
input_from_file = file_input_function()

# ask the user if they want the program to automatically remove invalid characters from the DNA
remove_errors = invalid_removal_choice_function()

#input for the DNA from the file or the consol
DNA = input_file_consol_function(input_from_file)

#everything for handling errors in the DNA
DNA = remove_errors_function(DNA, remove_errors, input_from_file)

#gives info about the DNA
DNA = DNA_info_function(DNA)

#let the user pick if they want the full codons to be read or only inbetween start-stop
read_start_stop = start_stop_reader_choice()

#turns the DNA into codons
codons = DNA_to_codons_function(DNA, read_start_stop, input_from_file)

#turns the codons in amino acids
amino_acids = codons_to_amino_acids_function(codons, input_from_file, codon_table_single, codon_table_short, codon_table_full)