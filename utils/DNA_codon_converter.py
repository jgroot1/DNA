def DNA_to_codons_function(DNA,read_start_stop, input_from_file):

    RNA = DNA.replace("T", "U")
    codons = [RNA[x:x+3] for x in range(0, len(RNA), 3)]

    if read_start_stop:
        read = False
        codons_read_between_start_stop = []
        for single_codons in codons:
            if not read and single_codons == "AUG":
                read = True
            elif read and single_codons in ["UAA", "UGA", "UAG"]:
                read = False
            else:
                if read:
                    codons_read_between_start_stop.append(single_codons)
        codons = codons_read_between_start_stop

    if len(codons) == 0:
        print("Codon count became 0 after reading in between start and stop codons.")
        raise SystemExit

    if input_from_file:
        file_path = "codons.txt"
        with open(file_path, "w") as codons_file:
            codons_file.write(str(codons))
            print("Codons written to file: 'codons.txt'")
            return codons

    else:
        print("codons:", codons)
        return codons