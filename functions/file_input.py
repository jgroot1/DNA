def file_input():

    input_type_chosen = False
    while input_type_chosen is False:

        try:
            input_from_file = input("Would you like to import DNA from a file? (Make sure to read the readme) (y/n): ").lower()

            if input_from_file in ["y", "yes"]:
                #check if the file for the input exists
                try:
                    with open("../DNA_input_file.txt", "r") as f:
                        print("Reading DNA from file.")
                except FileNotFoundError:
                    print("DNA_input_file.txt' Was not found")
                    raise SystemExit

                input_from_file = True
                input_type_chosen = True

            elif input_from_file in ["n", "no"]:
                input_from_file = False
                input_type_chosen = True
            else:
                raise ValueError
        except ValueError:
            print("Please enter either 'y' or 'n' for yes or no.")

    return input_from_file
