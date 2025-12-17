def find_neighbours(lines, l, i):
    neighbours = ''
    # Higher line
    if not l-1 < 0:
        neighbours += lines[l-1][i]
        if not i-1 < 0:
            neighbours += lines[l-1][i-1]
        if not i+1 > len(lines[0])-1:
            neighbours += lines[l-1][i+1]
    # Same Line
    if not i-1 < 0:
        neighbours += lines[l][i-1]
    if not i+1 > len(lines[0])-1:
        neighbours += lines[l][i+1] 
    # Lower Line
    if not l+1 > len(lines)-1:
        neighbours += lines[l+1][i]
        if not i-1 < 0:
            neighbours += lines[l+1][i-1]
        if not i+1 > len(lines[0])-1:
            neighbours += lines[l+1][i+1]
    return neighbours

def main():
    with open("day_4/input.txt", 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]
    num_rm_rolls = 0
    for l in range(len(lines)):
        for i in range(len(lines[0])):
            neighbours = find_neighbours(lines, l, i)
            count = neighbours.count('@')
            if count < 4 and lines[l][i] == '@':
                num_rm_rolls += 1
                #lines[l][i] = '.'
    print(num_rm_rolls)

if __name__ == "__main__":
    main()