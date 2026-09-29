from pathlib import Path

from utils.amino_acid_table_styles import *
from utils.cleaner import *

# converts the codons into amino acids
def codons_to_amino_acids_function(codon, input_from_file, table_style):
    amino_acids, amino_acid_full_name = [], []

    # convert the codons and list of codons if the codons are being read between start stop into amino acids
    while not amino_acid_full_name:

        if type(codon[0]) == str:
            amino_acids = amino_acid_table_style(codon, table_style)
            # needed for the amino acid information
            amino_acid_full_name = amino_acid_table_style(codon, "full")

        elif type(codon[0]) == list:
            for single_codon in codon:
                amino_acids.append(amino_acid_table_style(single_codon, table_style))
                # needed for the amino acid information
                amino_acid_full_name.append(amino_acid_table_style(single_codon, "full"))

    # outputs the amino acids in an easy-to-read way
    clean_amino_acids = clean(amino_acids)

    if not input_from_file:
        print("\namino acids:","\n", clean_amino_acids, "\n")

    # creates and writes the amino acids to amino_acids.txt
    if input_from_file:
        program_folder = Path(__name__).parent
        output_folder = program_folder / "output"
        output_folder.mkdir(exist_ok=True)
        with open(output_folder / "amino_acids.txt", "w") as f:
            f.write(clean_amino_acids)

    return amino_acids, amino_acid_full_name
