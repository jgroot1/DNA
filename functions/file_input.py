def file_input():

    input_from_file = None
    while input_from_file is None:
        try:
            input_from_file = input("Would you like to import DNA from a file? (Make sure to read the readme) (y/n): ").lower()
            if input_from_file in ["y", "yes"]:
                try:
                    with open("DNA_input_file.txt", "r"):
                        print("Reading DNA from file.")
                except FileNotFoundError:
                    print("DNA_input_file.txt' Was not found")
                    raise SystemExit
                input_from_file = True
            elif input_from_file in ["n", "no"]:
                input_from_file = False
            else:
                raise ValueError
        except ValueError:
            print("Please enter either 'y' or 'n' for yes or no.")

    return input_from_file
