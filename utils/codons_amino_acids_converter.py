def codons_to_amino_acids_function(codons, input_from_file, codon_table_single, codon_table_short, codon_table_full):
    amino_acids = []
    while not amino_acids:
        try:
            table_style = input("\nHow do you want the amino acid names: full/short/single: ").lower()
            if table_style in ["full", "short", "single"]:
                for codon in codons:
                    if table_style == "full":
                        amino_acids = [codon_table_full.get(x) for x in codon]
                    elif table_style == "short":
                        amino_acids = [codon_table_short.get(x) for x in codon]
                    elif table_style == "single":
                        amino_acids = [codon_table_single.get(x) for x in codon]
            else:
                raise ValueError
        except ValueError:
            print("Please enter one of these: full/short/single")

    if not input_from_file:
        print("\namino_acids:", amino_acids)
    if input_from_file:
        file_path = "amino_acids.txt"
        with open(file_path, "w") as amino_acids_file:
            amino_acids_file.write(str(amino_acids))
            print("Amino acids written to file: 'amino_acids.txt'")
    return amino_acids