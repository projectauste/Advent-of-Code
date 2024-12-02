def main():
    with open('input.txt') as file:
        content = [[int(n) for n in line.split(" ")] for line in file.readlines()]

    # safe_values = sum(safety_check(line) for line in content)

    # with open('output.txt', 'w') as file:
    #     file.write(str(safe_values))

    safe_values = sum(safety_check(line, 1) for line in content)
    print(safe_values)

def level(line, increase, dampner=0):
    if len(line) == 1:
        return True
    value = (line[1] - line[0] if increase else line[0] - line[1]) in [1, 2, 3]

    if value not in [1, 2, 3] and dampner == 1:
        dampner = 0
        value = True

    return value and level(line[1:], increase)


def safety_check(line, dampner=0):
    return level(line, True, dampner) or level(line, False, dampner)

if __name__ == '__main__':
    main()