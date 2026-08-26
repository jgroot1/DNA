def choose(prompt, positive, negative):
    picked = None
    while picked is None:
        try:
            picked = input(prompt + " (y/n): ").lower()
            if picked in ["y", "yes"]:
                print(positive)
                picked = True
            elif picked in ["n", "no"]:
                print(negative)
                picked = False
            else:
                raise ValueError
        except ValueError:
            print("Please enter either yes or no.\n")
            picked = None
    return picked
