from utils.codons_table import *
def amino_acids_info(amino_acids):
    def info(amino_acids):
        for amino_acid in full_amino_acid_list:
            # makes sure that only amino acids that are in the list wil be counted, else there will say for all the non-included that there are 0
            if amino_acids.count(amino_acid) > 0:
                print(f"Amount of {amino_acid}: {amino_acids.count(amino_acid)}, Percentage: {round(amino_acids.count(amino_acid) / len(amino_acids) * 100, 2)}%")
        print(f"Total is: {len(amino_acids)}\n")

    # used when the amino acids are in a single list
    if type(amino_acids[0]) == str:
        info(amino_acids)

    # used when the amino acids are in multiable proteins
    elif type(amino_acids[0]) == list:
        print("full amino acids information:")
        amino_acids_list = []
        for single_list in amino_acids:
            amino_acids_list += single_list
        info(amino_acids_list)
        # print the info for every single protein
        count = 0
        print("lose amino acids information:")
        for amino_acid in amino_acids:
            count += 1
            print("protein:", count)
            info(amino_acid)