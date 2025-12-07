# Day 1 part 2

dial_wrap = 100
dial_current_state = 50

def turn_left():
    return (dial_current_state - 1) % dial_wrap

def turn_right():
    return (dial_current_state + 1) % dial_wrap

def main():
    global dial_current_state
    counter = 0
    function_array = {'R': turn_right, 'L': turn_left}

    with open("day_1/input.txt") as t:
        for line in t:
            for i in range(int(line[1:])):
                dial_current_state = function_array[line[0]]()
                if dial_current_state == 0:
                    counter += 1

    print(counter)

if __name__ == "__main__":
    main()