
def find_highest_possible_jolt(input, k=12):
    
    numbers = [0] * k
    for i, n in enumerate(input):
        for l, a in enumerate(numbers):
            if n > a and len(input[i+1:]) >= len(numbers[l+1:]):
                numbers[l] = n
                numbers[l+1:] = [0]*len(numbers[l+1:])
                break

    sum = 0
    for i, a in enumerate(reversed(numbers)):
        sum += (10**i) * a
    print(sum)
    return sum

def main():
    total_jolts = 0
    with open("day_3/input.txt") as t:
        for line in t:
            numbers = list(map(int, list(line.strip())))
            total_jolts += find_highest_possible_jolt(numbers)
    print(total_jolts)

if __name__ == "__main__":
    main()