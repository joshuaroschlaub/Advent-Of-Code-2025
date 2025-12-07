# Day 1

dial_wrap = 100
dial_current_state = 50

def turn_left(n: int):
    return (dial_current_state - n) % dial_wrap

def turn_right(n: int):
    return (dial_current_state + n) % dial_wrap

def main():
    global dial_current_state
    counter = 0
    function_array = {'R': turn_right, 'L': turn_left}

    with open("day_1/input.txt") as t:
        for line in t:
            dial_current_state = function_array[line[0]](int(line[1:]))
            if dial_current_state == 0:
                counter += 1

    print(counter)

if __name__ == "__main__":
    main()