from pathlib import Path

from utils.amino_acid_table_styles import *
from utils.cleaner import *

def codons_to_amino_acids_function(codon, input_from_file, table_style):

    amino_acids = []
    amino_acid_full_name = []
    codons = codon

    while not amino_acid_full_name:
        if type(codon[0]) == list:
            for codon in codons:
                amino_acids.append(amino_acid_table_style(codon, table_style))
                # needed for the amino acid information
                amino_acid_full_name.append(amino_acid_table_style(codon, "full"))

        else:
            amino_acids = amino_acid_table_style(codon, table_style)
            # needed for the amino acid information
            amino_acid_full_name = amino_acid_table_style(codon, "full")


    clean_amino_acids = clean(amino_acids)

    if not input_from_file:
        print("\namino acids:", clean_amino_acids,"\n")

    if input_from_file:
        program_folder = Path(__name__).parent
        output_folder = program_folder / "output"
        output_folder.mkdir(exist_ok=True)

        with open(output_folder / "amino_acids.txt", "w") as f:
            f.write(clean_amino_acids)

    return amino_acids, amino_acid_full_name
