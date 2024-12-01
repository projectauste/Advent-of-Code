import sys
sys.setrecursionlimit(1500)

with open('input.txt') as f:
    id_list_1, id_list_2 = zip(*[map(int, line.split()) for line in f])
    id_list_1 = sorted(id_list_1)
    id_list_2 = sorted(id_list_2)

def add_id(id_list_1, id_list_2) -> int:
    if not id_list_1 or not id_list_2:
        return 0

    return abs(id_list_1[0] - id_list_2[0]) + add_id(id_list_1[1:], id_list_2[1:])

sum = add_id(id_list_1, id_list_2)

with open('output.txt', 'w') as f:
    f.write(str(sum))