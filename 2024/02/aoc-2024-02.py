import copy

def main():
    with open('input.txt') as file:
        content = [[int(n) for n in line.split(" ")] for line in file.readlines()]

    # safe_values = sum(safety_check(line) for line in content)

    # with open('output.txt', 'w') as file:
    #     file.write(str(safe_values))
    safe_values = []
    safe_value_lines = []
    for line in content:
        value = safety_check(line)
        if value == True or dampener(line) == True:
            safe_values.append(value)
        else:
            print(value, line)
        # else:
            # print(line, value)
    # safe_values = [True for line in content if safety_check(line)]

    # dictionary = {}
    # for i in safe_values:
    #     dictionary[str(i)] = safe_values.count(i)
    #
    # print(dictionary)

    print(len(safe_values))
def level(line, increase):
    if not line or len(line) == 1:
        return True
    value = (line[1] - line[0] if increase else line[0] - line[1]) in [1, 2, 3]

    return value and level(line[1:], increase)


def safety_check(line):
    value = level(line, True) or level(line, False)
    # print(line)
    # print(value)

    return value

def dampener(line):
    new_line = line.copy()
    for i in range(len(line)):
        new_line.remove(line[i])
        print(new_line)
        if safety_check(new_line) == True:
            return True
        new_line = line.copy()


# Go over every unsafe data.
# Remove the first element, if the rest counts as safe, mark the original list as safe
# If not, remove the second element, test, so on and so forth until out of elements.
# if all unsafe, keep unsafe

if __name__ == '__main__':
    main()