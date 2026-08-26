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
        file_path = "amino_acids.txt"
        with open(file_path, "w") as amino_acids_file:
            amino_acids_file.write(str(amino_acids))
            print("Amino acids written to file: 'amino_acids.txt'")
    return amino_acids
