def DNA_to_codons_function(DNA, input_from_file):

    RNA = DNA.replace("T", "U")
    codons = [RNA[x:x+3] for x in range(0, len(RNA), 3)]
    if input_from_file:
        file_path = "codons.txt"
        with open(file_path, "w") as codons_file:
            codons_file.write(str(codons))
            print("Codons written to file: 'codons.txt'")
            return codons
    elif not input_from_file:
        print("codons:", codons)
        return codons