import re

def main():
    with open("input.txt") as f:
        matches = re.findall(r"mul\(\d+,\d+\)", f.read())

    result = sum(eval(match) for match in matches)

    with open("output.txt", "w") as f:
        f.write(str(result))


def mul(n1, n2):
    return n1 * n2


if __name__ == "__main__":
    main()




