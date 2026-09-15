from pathlib import Path

def DNA_to_codons_function(DNA, read_start_stop, input_from_file):
    RNA = DNA.replace("T", "U")
    codons = [RNA[x:x + 3] for x in range(0, len(RNA), 3)]

    if read_start_stop:
        read = False
        codon_list = []
        codons_read_between_start_stop = []
        for single_codons in codons:
            if read and single_codons in ["UAA", "UGA", "UAG"]:
                codon_list.append(codons_read_between_start_stop.copy())
                codons_read_between_start_stop.clear()
                read = False
            if read:
                codons_read_between_start_stop.append(single_codons)
            if not read and single_codons == "AUG":
                read = True

        if len(codon_list) == 1:
            codon_list = codon_list[0]
        codons = codon_list

    if len(codons) == 0:
        print("Codon count became 0 after reading in between start and stop codons.")
        input("press enter to close program")
        raise SystemExit(1)


    if not input_from_file:
        print("codons:", codons)

    if input_from_file:
        program_folder = Path(__name__).parent
        output_folder = program_folder / "output"
        output_folder.mkdir(exist_ok=True)

        with open(output_folder / "codons.txt", "w") as f:
            f.write(str(codons))

    return codons