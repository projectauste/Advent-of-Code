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

# def safety_check(line):
#     value = higher(line, 1) or lower(line, 1)
#
#     return value
#
# def higher(line, dampner=0):
#     i = 0
#     values = []
#     while i < len(line):
#         if i + 1 >= len(line):
#             return True
#
#         value = line[i + 1] - line[i] in [1, 2, 3]
#         if value == False:
#             if dampner == 1:
#                 if line[i + 2] - line[i] in [1, 2, 3]:
#                     line.pop(i+1)
#                 dampner = 0
#                 continue
#
#         i += 1
#         values.append(value)
#     if False in values:
#         return False
#     else:
#         return True
#
# def lower(line, dampner=0):
#     i = 0
#     values = []
#     while i < len(line):
#         if i + 1 >= len(line):
#             return True
#
#         value = line[i] - line[i + 1] in [1, 2, 3]
#         if value == False:
#             if dampner == 1:
#                 if line[i] - line[i + 2] in [1, 2, 3]:
#                     line.pop(i)
#                 dampner == 0
#                 continue
#
#         i += 1
#         values.append(value)
#
#     if False in values:
#         return False
#     else:
#         return True





if __name__ == '__main__':
    main()