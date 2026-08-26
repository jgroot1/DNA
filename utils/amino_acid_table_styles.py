def amino_acid_table_style(codons, table_style, codon_table_full, codon_table_short, codon_table_single):
    amino_acids = []
    if table_style == "full":
        amino_acids = [codon_table_full.get(single_codon) for single_codon in codons]
    elif table_style == "short":
        amino_acids = [codon_table_short.get(single_codon) for single_codon in codons]
    elif table_style == "single":
        amino_acids = [codon_table_single.get(single_codon) for single_codon in codons]

    return amino_acids
