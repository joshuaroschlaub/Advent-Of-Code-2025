
def find_highest_possible_jolt(numbers):
    a = 0
    b = 0
    for i, x in enumerate(numbers):
        if x > a and not i == len(numbers)-1:
            a = x
            b = numbers[i+1]
        elif x > b:
            b = x
    return a*10+b

def main():
    total_jolts = 0
    with open("day_3/input.txt") as t:
        for line in t:
            numbers = list(map(int, list(line)[:-1]))
            total_jolts += find_highest_possible_jolt(numbers)
    print(total_jolts)

if __name__ == "__main__":
    main()