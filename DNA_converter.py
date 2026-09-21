from utils.DNA_codon_converter import *
from utils.DNA_info import *
from utils.DNA_input import *
from utils.amino_acid_name_style import *
from utils.codons_amino_acids_converter import *
from utils.error_removal import *
from utils.yes_no import *

def main():
    # ask the user if they want to import their DNA from a file or the console
    input_from_file = choose(
        "Do you want to input the DNA from a file?",
        "Reading DNA from file",
        "Reading DNA from console")

    # ask the user if they want the program to automatically remove invalid characters from the DNA
    remove_errors = choose(
        "Do you want to automatically remove invalid characters from the DNA?",
        "Automatically removing invalid characters from the DNA",
        "Keeping invalid characters in DNA, This can cause errors and the program will close when that happens")

    # input for the DNA from the file or the consol
    DNA = input_file_consol_function(input_from_file)

    # everything for handling errors in the DNA
    DNA = remove_errors_function(DNA, remove_errors, input_from_file)

    # gives info about the DNA
    DNA = DNA_info_function(DNA)

    # let the user pick if they want the full codons to be read or only inbetween start-stop
    read_start_stop = choose(
        "Do you want the codons to be read between the start/stop codons",
        "Reading DNA between start/stop",
        "Keeping full DNA")

    # turns the DNA into codons
    codons = DNA_to_codons_function(DNA, read_start_stop, input_from_file)

    # ask how the amino acids should be displayed
    table_style = amino_acid_name_style()

    # turns the codons in amino acids
    amino_acids = codons_to_amino_acids_function(codons, input_from_file, table_style)

    input("\nprogram finished successfully press enter to close the program")


if __name__ == "__main__":
    main()
