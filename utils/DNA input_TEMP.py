DNA_entered = False
while DNA_entered is False:
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

    if error:
        print("Please enter valid DNA\n")
        if input_from_file:
            print("Invalid DNA entered from file. Please try again.")
            raise SystemExit