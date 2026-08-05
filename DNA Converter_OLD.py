#ask the user if they want to input DNA from a input() or a file
input_from_file = None
while input_from_file is None:
    try:
        input_from_file = input("Would you like to import DNA from a file? (Make sure to read the readme) (y/n): ").lower()
        if input_from_file in ["y", "yes"]:
            #check if the file for the input exists
            try:
                with open("DNA_input_file.txt", "r"):
                    print("Reading DNA from file.")
            except FileNotFoundError:
                print("DNA_input_file.txt' Was not found")
                raise SystemExit
            input_from_file = True

        elif input_from_file in ["n", "no"]:
            input_from_file = False
        else:
            input_from_file = None
            raise ValueError
    except ValueError:
        print("Please enter either 'y' or 'n' for yes or no.")

#ask the user if they want to remove invalid characters from the DNA that is being read
remove_errors = None
while remove_errors is None:
    try:
        remove_errors = input("\nDo you want to automatically remove invalid characters from the DNA?: (y/n): ").lower()
        if remove_errors in ["y", "yes"]:
            print("Automatically removing invalid characters from the DNA")
            remove_errors = True
        elif remove_errors in ["n", "no"]:
            print("Keeping invalid characters in DNA\n")
            remove_errors = False
        else:
            remove_errors = None
            raise ValueError
    except ValueError:
        print("Please enter either 'y' or 'n' for yes or no.")

#input for the dna
DNA_entered = None
while DNA_entered is None:
    error = False

    if not input_from_file:
        DNA = input("\nEnter DNA: ").upper()
    elif input_from_file:
        try:
            with open("DNA_input_file.txt", "r") as f:
                DNA = f.read().upper()
        except FileNotFoundError:
            print("'DNA_input_file.txt' file not found, please try again and make sure to read the readme.")
            raise SystemExit

    if len(DNA) <3:
        print("Please enter DNA that is longer than 3 characters.")
        error = True

    if remove_errors:
        errors_found = 0
        valid_DNA = ""
        for character in DNA:
            if character in "ATCG":
                valid_DNA += character
            else:
                errors_found += 1
        if len(valid_DNA) < 3:
            #if not errors makes sure that a DNA too short error can only print once
            if not error:
                print("DNA became shorter than 3 characters after removing invalid characters.")
                error = True
        if not error:
            print(f"\n{errors_found} Invalid characters removed from DNA")
            DNA = valid_DNA
            DNA_entered = True

    elif not remove_errors:
        invalid_characters = ""
        for num, character in enumerate(DNA, start=1):
            if character not in "ATCG":
                if not input_from_file:
                    print((character, "Is not valid DNA, it is character nr:", num))
                    error = True
                elif input_from_file:
                    invalid_characters += f"{character} Is not valid DNA, it is character nr: {num}"
                    error = True

    if input_from_file and invalid_characters != "":
        file_path = "Invalid_characters.txt"
        with open(file_path, "w") as errors_file:
            errors_file.write(invalid_characters)
            print("Invalid characters written to file: 'Invalid_characters.txt' ")

    if not error:
        DNA_entered = True
    elif error:
        print("Please enter valid DNA\n")
        if input_from_file:
            print("Invalid DNA entered from file. Please try again.")
            raise SystemExit

#remove any characters that won't form a codon
remainder = len(DNA) % 3
if remainder != 0:
    print(DNA[len(DNA) - remainder], "Was removed form the end of the DNA, because it is too short to form a codon\n")
    DNA = DNA[:-remainder]

#gives information about the dna
for character in ["A", "T", "C", "G"]:
    print(f"Amount of {character}: {DNA.count(character)}, Percentage: {round(DNA.count(character)/len(DNA) * 100 ,2)}%")
print(f"Total is: {len(DNA)}\n")


#turn the DNA into RNA and returning it in the form of codons
RNA = DNA.replace("T", "U")
codons = [RNA[x:x+3] for x in range(0, len(RNA), 3)]
if not input_from_file:
    print("codons:",codons)
if input_from_file:
    file_path = "codons.txt"
    with open(file_path, "w") as codons_file:
        codons_file.write(str(codons))
        print("Codons written to file: 'codons.txt'")

#turn the codons into amino acids
from utils.codons_table import codon_table_single, codon_table_short, codon_table_full
amino_acids = []
while not amino_acids:
    try:
        table_style = input("\nHow do you want the amino acid names: full/short/single: ").lower()

        if table_style == "full":
            amino_acids = [codon_table_full.get(x) for x in codons]
        elif table_style == "short":
            amino_acids = [codon_table_short.get(x) for x in codons]
        elif table_style == "single":
            amino_acids = [codon_table_single.get(x) for x in codons]
        else:
            raise ValueError
    except ValueError:
        print("Please enter one of these: full/short/single")

if not input_from_file:
    print("\namino_acids:",amino_acids)
if input_from_file:
    file_path = "amino_acids.txt"
    with open(file_path, "w") as amino_acids_file:
        amino_acids_file.write(str(amino_acids))
        print("Amino acids written to file: 'amino_acids.txt'")