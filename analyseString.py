def analyse_string(string) :
    num_of_lowercased = 0
    num_of_uppercased = 0

    for char in string :
        if char.islower() : num_of_lowercased += 1
        else :
            if char.isupper() : num_of_uppercased += 1
    return num_of_lowercased, num_of_uppercased


if __name__ == "__main__" :
    text = input("Enter your text here: ")
    lowercased_chars, uppercased_chars = analyse_string(text)
    print("\nThere are ", lowercased_chars, " lower cased characters and "\
        , uppercased_chars, " upper cased characters in the string '", text,"'.")