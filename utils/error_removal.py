from pathlib import Path

def remove_errors_function(DNA, remove_errors, input_from_file):
    error = False
    if remove_errors:
        errors_found = 0
        valid_DNA = ""
        for character in DNA:
            if character in "ATCG":
                valid_DNA += character
            else:
                errors_found += 1

        if len(valid_DNA) < 3:
            print("DNA became shorter than 3 characters after removing invalid characters.")
            error = True

        print(errors_found, "Invalid characters removed from DNA")
        DNA = valid_DNA

    elif not remove_errors:
        invalid_characters = ""
        for num, character in enumerate(DNA, start=1):
            if character not in "ATCG":
                if not input_from_file:
                    print(f"'{character}' Is not valid DNA, it is character nr: {num}")
                    error = True
                elif input_from_file:
                    invalid_characters += f"{character} Is not valid DNA, it is character nr: {num}\n"
                    error = True

        if input_from_file and invalid_characters != "":
            program_folder = Path(__name__).parent
            output_folder = program_folder / "output"
            output_folder.mkdir(exist_ok=True)

            with open(output_folder / "Invalid_characters.txt", "w") as f:
                f.write(str(invalid_characters))

    if error:
        print("Please enter valid DNA\n")
        if input_from_file:
            print("Invalid DNA entered from file. Please try again.")
        else:
            print("Invalid DNA entered from console. Please try again.")
        input("press enter to close program")
        raise SystemExit

    else:
        return DNA
