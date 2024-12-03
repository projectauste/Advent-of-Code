import re

def main():
    with open("input.txt") as f:
        matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", f.read())

    result = add(matches)

    with open("output.txt", "w") as f:
        f.write(str(result))

def add(matches, do=True):
    if not matches:
        return 0

    if do == False:
        if matches[0] == "do()":
            do = True
        return add(matches[1:], do)

    result = eval(matches[0]) if matches[0].startswith("mul") else 0

    if matches[0] == "don't()":
        do = False

    return result + add(matches[1:], do)

def mul(n1, n2):
    return n1 * n2


if __name__ == "__main__":
    main()




