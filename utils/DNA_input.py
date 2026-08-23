def input_file_consol_function(input_from_file):
    DNA_entered = False
    while not DNA_entered:
        if not input_from_file:
            DNA = input("Enter DNA: ").upper()
        elif input_from_file:
            try:
                with open("DNA_input_file.txt", "r") as f:
                    DNA = f.read().upper()
            except FileNotFoundError:
                print("'DNA_input_file.txt' file not found, please try again and make sure to read the readme.")
                raise SystemExit(1)
        if len(DNA) < 3:
            print("Please enter DNA that is longer than 3 characters.")
            if input_from_file is True:
                print("The DNA entered from file is shorter than 3, Please check the file if everything is correct.")
                raise SystemExit(1)
        else:
            DNA_entered = True
    return DNA
