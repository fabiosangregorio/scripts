import os


def anki_format(input):
    splitted = input.split("$")
    output = ""
    for index, substring in enumerate(splitted):
        if index == len(splitted) - 1:
            delimiter = ""
        elif index % 2 == 0:
            delimiter = "[$]"
        else:
            delimiter = "[/$]"
        output += substring + delimiter
    return output


if __name__ == "__main__":
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_PATH, "input_output.txt")
    with open(file_path) as f:
        input = f.read()

    output = anki_format(input)

    with open(file_path, "w") as f:
        f.write(output)
