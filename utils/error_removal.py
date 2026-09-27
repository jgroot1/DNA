from pathlib import Path

# makes sure that characters that can't be in DNA won't be entered
def remove_errors_function(DNA, remove_errors, input_from_file):

    # automatically removes all the invalid characters
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

    # used when the user does not want to automatically remove the errors
    elif not remove_errors:
        invalid_characters = ""
        for num, character in enumerate(DNA, start=1):

            # outputs the invalid characters
            if character not in "ATCG":
                if not input_from_file:
                    print(f"'{character}' Is not valid DNA, it is character nr: {num}")
                    error = True
                elif input_from_file:
                    invalid_characters += f"{character} Is not valid DNA, it is character nr: {num}\n"
                    error = True

        # creates and writes the invalid characters to invalid_characters.txt
        if input_from_file and invalid_characters != "":
            program_folder = Path(__name__).parent
            output_folder = program_folder / "output"
            output_folder.mkdir(exist_ok=True)
            with open(output_folder / "invalid_characters.txt", "w") as f:
                f.write(str(invalid_characters))

    # closes the program if the DNA is shorter than 3 or has invalid characters when they are kept
    if error:
        print("Please enter valid DNA\n")
        if input_from_file:
            print("Invalid DNA entered from file. Please try again.")
        elif not input_from_file:
            print("Invalid DNA entered from console. Please try again.")
        input("press enter to close program")
        raise SystemExit(1)

    else:
        return DNA
