from utils.codon_amino_acid_tables import *

# convert the codons into the chosen table style
def amino_acid_table_style(codons, table_style):
    amino_acids = []
    if table_style == "full":
        amino_acids = [codon_table_full.get(single_codon) for single_codon in codons]
    elif table_style == "short":
        amino_acids = [codon_table_short.get(single_codon) for single_codon in codons]
    elif table_style == "single":
        amino_acids = [codon_table_single.get(single_codon) for single_codon in codons]

    return amino_acids
