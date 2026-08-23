"""
[AUG] =                          start/Met, M
[UAA, UGA, UAG] =                stop
[UUU, UUC] =                     [Phenylalanine, Phe, F]
[UUA, UUG, CUU, CUC, CUA, CUG] = [Leucine, Leu, L]
[UCU, UCC, UCA, UCG, AGU, AGC] = [Serine, Ser, S]
[UAU, UAC] =                     [Tyrosine, Tyr, Y]
[UGU, UGC] =                     [Cysteine, Cys, C]
[UGG] =                          [Tryptophan, Trp, W]
[CCU, CCC, CCA, CCG] =           [Proline, Pro, P]
[CAU, CAC] =                     [Histidine, His, H]
[CAA, CAG] =                     [Glutamine, Gln, Q]
[CGU, CGC, CGA, CGG, AGA, AGG] = [Arginine, Arg, R]
[AUU, AUC, AUA] =                [Isoleucine, Ile, I]
[ACU, ACC, ACA, ACG] =           [Threonine, Thr, T]
[AAU, AAC] =                     [Asparagine, Asn, N]
[AAA, AAG] =                     [Lysine, Lys, K]
[GUU, GUC, GUA, GUG] =           [Valine, Val, V]
[GCU, GCC, GCA, GCG] =           [Alanine, Ala, A]
[GAU, GAC] =                     [Aspartic acid, Asp, D]
[GAA, GAG] =                     [Glutamic acid, Glu, E]
[GGU, GGC, GGA, GGG] =           [Glycine, Gly, G]
"""

codon_table_full = {
    "AUG": "Methionine",
    "UAA": "stop", "UGA": "stop", "UAG": "stop",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine", "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "AGU": "Serine", "AGC": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
    "CAU": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine", "AGA": "Arginine", "AGG": "Arginine",
    "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine",
    "ACU": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
    "AAU": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine",
    "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
    "GAU": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine"
}

codon_table_short = {
    "AUG": "Met",
    "UAA": "stop", "UGA": "stop", "UAG": "stop",
    "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "AGU": "Ser", "AGC": "Ser",
    "UAU": "Tyr", "UAC": "Tyr",
    "UGU": "Cys", "UGC": "Cys",
    "UGG": "Trp",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

codon_table_single = {
    "AUG": "M",
    "UAA": "stop", "UGA": "stop", "UAG": "stop",
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "UAU": "Y", "UAC": "Y",
    "UGU": "C", "UGC": "C",
    "UGG": "W",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}
