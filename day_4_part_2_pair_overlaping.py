input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def separate_numbers(list_of_2_el):
    return list(int(x) for x in list_of_2_el.split('-'))


input = input.split('\n')
overlap = 0

for i in input:
    el = i.split(',')
    pair = list(map(separate_numbers, el))
    
    pair_1_begin = pair[0][0]
    pair_1_end = pair[0][1]
    pair_2_begin = pair[1][0]
    pair_2_end = pair[1][1]

    if (pair_2_begin > pair_1_end) or (pair_2_end < pair_1_begin):
        overlap += 1
    elif (pair_1_begin > pair_2_end) or (pair_1_end < pair_2_begin):
        overlap += 1
        
overlap_total = len(input) - overlap
print(overlap_total)