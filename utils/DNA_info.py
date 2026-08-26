def DNA_info_function(DNA):
    # remove any characters that won't form a codon
    remainder = len(DNA) % 3
    if remainder != 0:
        print(DNA[-remainder:], "Was removed form the end of the DNA, because it is too short to form a codon\n")
        DNA = DNA[:-remainder]

    # gives information about the dna
    for character in ["A", "T", "C", "G"]:
        print(f"Amount of {character}: {DNA.count(character)}, Percentage: {round(DNA.count(character) / len(DNA) * 100, 2)}%")
    print(f"Total is: {len(DNA)}")
    return DNA
