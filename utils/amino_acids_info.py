from utils.codons_table import *

# gives information about the amino acids
def amino_acids_info(amino_acids):

    # the function that is used to give the info
    def info(full_amino_acids):
        for single_amino_acid in full_amino_acid_list:

            # makes sure that only amino acids that are in the list wil be counted, else there will say for all the non-included that there are 0
            if full_amino_acids.count(single_amino_acid) > 0:
                print(f"Amount of {single_amino_acid}: {full_amino_acids.count(single_amino_acid)}, Percentage: {round(full_amino_acids.count(single_amino_acid) / len(full_amino_acids) * 100, 2)}%")
        print(f"Total is: {len(full_amino_acids)}\n")

    # used when the amino acids are in a single list
    if type(amino_acids[0]) == str:
        info(amino_acids)

    # used when the amino acids are in multiple proteins
    elif type(amino_acids[0]) == list:
        print("full amino acids information:")
        amino_acids_list = []
        for single_list in amino_acids:
            amino_acids_list += single_list
        info(amino_acids_list)

        # print the info for every single protein
        count = 0
        print("protein information:\n")
        for amino_acid in amino_acids:
            count += 1
            print("protein:", count)
            info(amino_acid)
