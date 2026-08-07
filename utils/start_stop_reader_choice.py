def start_stop_reader_choice():
    read_start_stop = None
    while read_start_stop is None:
        try:
            read_start_stop = input("\nDo you want the codons to be read between the start/stop codons: (y/n): ").lower()
            if read_start_stop in ["y", "yes"]:
                print("Reading DNA between start/stop\n")
                read_start_stop = True
            elif read_start_stop in ["n", "no"]:
                print("Keeping full DNA\n")
                read_start_stop = False
            else:
                read_start_stop = None
                raise ValueError
        except ValueError:
            print("Please enter either 'y' or 'n' for yes or no.")
    return read_start_stop
