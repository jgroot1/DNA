# used to make the output of the codons and amino acids look better
def clean(to_clean):
    if type(to_clean[0]) == str:
        cleaned = " ".join(to_clean)

    elif type(to_clean[0]) == list:
        cleaned = ""
        for item in to_clean:
            cleaned_row = ""
            cleaned_row += " ".join(item)
            cleaned += cleaned_row + "\n"

    return cleaned
