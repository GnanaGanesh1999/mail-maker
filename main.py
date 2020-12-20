with open("./input/Names/invited_names.txt") as names_file:
    names = list(names_file.read().split("\n"))
    sample_file = open("./Input/Letters/sample_letter.txt")
    sample_letter = sample_file.read()
    print(sample_letter)
    sample_file.close()
    for name in names:
        with open(f"./Output/ReadyToSend/letter_for_{name}", "w") as output_file:
            content = sample_letter
            content = content.replace("[name]", name)
            output_file.write(content)