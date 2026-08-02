def remove_errors(DNA):
    error = False
    errors_found = 0
    valid_DNA = ""
    for character in DNA:
        if character in "ATCG":
            valid_DNA += character
        else:
            errors_found += 1
    if len(valid_DNA) < 3:
        # if not errors makes sure that a DNA too short error can only print once
        if not error:
            print("DNA became shorter than 3 characters after removing invalid characters.")
            error = True
    if not error:
        print(errors_found, "Invalid characters removed from DNA")
        DNA = valid_DNA
        DNA_entered = True
    return DNA
