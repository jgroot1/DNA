def DNA_to_codons_function(DNA,read_start_stop, input_from_file):

    RNA = DNA.replace("T", "U")
    codons = [RNA[x:x+3] for x in range(0, len(RNA), 3)]

    if read_start_stop:
        read = False
        codons_read_between_start_stop = []
        for single_codons in codons:
            if single_codons == "AUG":
                read = True
                print(single_codons)

            elif single_codons in ["UAA", "UGA", "UAG"]:
                read = False
                print(single_codons)
            else:
                if read:
                    codons_read_between_start_stop.append(single_codons)
        codons = codons_read_between_start_stop

    if input_from_file:
        file_path = "codons.txt"
        with open(file_path, "w") as codons_file:
            codons_file.write(str(codons))
            print("Codons written to file: 'codons.txt'")
            return codons

    else:
        print("codons:", codons)
        return codons