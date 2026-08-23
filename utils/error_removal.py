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
            file_path = "Invalid_characters.txt"
            with open(file_path, "w") as errors_file:
                errors_file.write(invalid_characters)
                print("Invalid characters written to file: 'Invalid_characters.txt' ")

    if error:
        print("Please enter valid DNA\n")
        if input_from_file:
            print("Invalid DNA entered from file. Please try again.")
            raise SystemExit
        else:
            print("Invalid DNA entered from consol. Please try again.")
            raise SystemExit
    else:
        return DNA