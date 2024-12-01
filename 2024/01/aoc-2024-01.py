import sys
sys.setrecursionlimit(1500)

with open('input.txt') as f:
    id_list_1, id_list_2 = zip(*[map(int, line.split()) for line in f])
    id_list_1 = sorted(id_list_1)
    id_list_2 = sorted(id_list_2)

def distance(id_list_1, id_list_2) -> int:
    if not id_list_1 or not id_list_2:
        return 0

    return abs(id_list_1[0] - id_list_2[0]) + distance(id_list_1[1:], id_list_2[1:])

def similarity(id_list_1, id_list_2) -> int:
    if not id_list_1 or not id_list_2:
        return 0

    count = id_list_2.count(id_list_1[0])
    return count * id_list_1[0] + similarity(id_list_1[1:], id_list_2)

distance_sum = distance(id_list_1, id_list_2)
similarity_sum = similarity(id_list_1, id_list_2)

with open('output.txt', 'w') as f:
    f.write(f'P1: {distance_sum}\nP2: {similarity_sum}')

