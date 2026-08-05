def invalid_removal_choice_function():
    remove_errors = None
    while remove_errors is None:
        try:
            remove_errors = input("\nDo you want to automatically remove invalid characters from the DNA?: (y/n): ").lower()
            if remove_errors in ["y", "yes"]:
                print("Automatically removing invalid characters from the DNA\n")
                remove_errors = True
            elif remove_errors in ["n", "no"]:
                print("Keeping invalid characters in DNA, This can cause errors!\n")
                remove_errors = False
            else:
                remove_errors = None
                raise ValueError
        except ValueError:
            print("Please enter either 'y' or 'n' for yes or no.")
    return remove_errors