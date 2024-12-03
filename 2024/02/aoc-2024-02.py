def main():
    with open('input.txt') as file:
        content = [[int(n) for n in line.split(" ")] for line in file.readlines()]

    # safe_values = sum(safety_check(line) for line in content)

    # with open('output.txt', 'w') as file:
    #     file.write(str(safe_values))
    safe_values = [True for line in content if safety_check(line)]
    print(len(safe_values))

def level(line, increase):
    if not line or len(line) == 1:
        return True
    value = (line[1] - line[0] if increase else line[0] - line[1]) in [1, 2, 3]

    return value and level(line[1:], increase)


def safety_check(line):
    value = level(line, True) or level(line, False)

    return value


if __name__ == '__main__':
    main()