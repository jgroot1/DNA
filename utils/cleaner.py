def clean(to_clean):
    if type(to_clean[0]) == str:
        cleaned = " ".join(to_clean)

    elif type(to_clean[0]) == list:
        cleaned = ""
        for item in to_clean:
            cleaned += "\n ".join(item)
    return cleaned
