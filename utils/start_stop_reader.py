def start_stop_reader(amino_acids):
    amino_acids_read_between_start_stop = ""
    for single_amino_acid in amino_acids:
        if single_amino_acid == "AUG":
            read = True
        elif single_amino_acid in ["UAA", "UGA", "UAG"]:
            read = False
        else:
            if read:
                amino_acids_read_between_start_stop += single_amino_acid
    amino_acids = amino_acids_read_between_start_stop