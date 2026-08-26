def among_acid_name_style():
    table_style = None
    while table_style is None:
        try:
            table_style = input("\nHow do you want the amino acid names: full/short/single: ").lower()
            if table_style not in ["full", "short", "single"]:
                raise ValueError
        except ValueError:
            print("Please enter one of these: full/short/single")
            table_style = None
    return table_style
