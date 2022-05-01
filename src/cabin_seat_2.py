from itertools import izip_longest

from pprint import pprint

blocks = [[2, 2], [4, 5], [2, 4], [2, 3], [6, 6]]
blocks = [[2, 3], [4, 4], [2, 4]]

# blocks = [[3,1],[4,4],[3,1]]


result = []
for i in range(len(blocks)):
    result.append([[0 for x in range(blocks[i][0]+1)] for y in range(blocks[i][1])])

result = list(izip_longest(*result, fillvalue=None))
pprint(result)

window = 1
isle_count = blocks[0][1] + blocks[-1][1] + 1
others = isle_count * 2 - 1 + sum([j * 2 for i, j in blocks[1:-1]])

print window,isle_count,others
print result
for index, row in enumerate(result):
    if row[0]:
        row[0][0] = window
        window += 1

    for ind, col in enumerate(row):
        if col:
            if ind != 0:
                col[0] = isle_count
                isle_count += 1

            for i in range(1, len(col) - 1):
                col[i] = others + i
                others += 1

            if ind != len(row) - 1:
                col[-1] = isle_count
                isle_count += 1

    if row[-1]:
        row[-1][-1] = window
        window += 1

pprint(result)

