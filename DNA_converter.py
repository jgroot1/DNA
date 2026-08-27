from utils.DNA_codon_converter import DNA_to_codons_function
from utils.DNA_info import DNA_info_function
from utils.DNA_input import input_file_consol_function
from utils.amino_acid_name_style import among_acid_name_style
from utils.codons_amino_acids_converter import codons_to_amino_acids_function
from utils.codons_table import codon_table_single, codon_table_short, codon_table_full
from utils.error_removal import remove_errors_function
from utils.yes_no import choose

# ask the user if they want to import their DNA from a file or the consol
input_from_file = choose(
    "Do you want to input the DNA from a file?",
    "Reading DNA from file",
    "Reading DNA from console")

# ask the user if they want the program to automatically remove invalid characters from the DNA
remove_errors = choose(
    "\nDo you want to automatically remove invalid characters from the DNA?",
    "Automatically removing invalid characters from the DNA\n",
    "Keeping invalid characters in DNA, This can cause errors and the program will close when that happens\n")

# input for the DNA from the file or the consol
DNA = input_file_consol_function(input_from_file)

# everything for handling errors in the DNA
DNA = remove_errors_function(DNA, remove_errors, input_from_file)

# gives info about the DNA
DNA = DNA_info_function(DNA)

# let the user pick if they want the full codons to be read or only inbetween start-stop
read_start_stop = choose(
    "\nDo you want the codons to be read between the start/stop codons",
    "Reading DNA between start/stop\n",
    "Keeping full DNA\n")

# turns the DNA into codons
codons = DNA_to_codons_function(DNA, read_start_stop, input_from_file)

# ask in how the amino acids should be displayed
table_style = among_acid_name_style()

# turns the codons in amino acids
amino_acids = codons_to_amino_acids_function(codons, input_from_file, table_style, codon_table_full, codon_table_short,codon_table_single)
