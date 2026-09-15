from pathlib import Path
from utils.amino_acid_table_styles import amino_acid_table_style

def codons_to_amino_acids_function(codon, input_from_file, table_style, codon_table_full, codon_table_short,codon_table_single):

    amino_acids = []
    codons = codon

    while not amino_acids:
        if type(codon[0]) == list:
            for codon in codons:
                amino_acids.append(amino_acid_table_style(codon, table_style, codon_table_full, codon_table_short, codon_table_single))

        else:
            amino_acids = amino_acid_table_style(codon, table_style, codon_table_full, codon_table_short,codon_table_single)

    if not input_from_file:
        print("\namino_acids:", amino_acids)

    if input_from_file:
        program_folder = Path(__name__).parent
        output_folder = program_folder / "output"
        output_folder.mkdir(exist_ok=True)

        with open(output_folder / "amino_acids.txt", "w") as f:
            f.write(str(amino_acids))

    return amino_acids
