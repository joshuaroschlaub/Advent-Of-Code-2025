# Day 1 problem 2

def id_is_invalid(id):
    id = str(id)
    length = len(id)
    
    for i in range(1, length//2 + 1):
        substring = id[:i]
        if substring * (length//i) == id:
            return True
    else:
        return False

def main():
    f = open("day_2/input.txt").readline()
    ranges = f.split(',')
    invalid_ids = []

    for ranges_element in ranges:
        start_id = int(ranges_element.split('-')[0])
        end_id = int(ranges_element.split('-')[1])
        id_list = list(range(start_id, end_id+1))
        for id in id_list:
            if id_is_invalid(id):
                invalid_ids.append(id)
    print(sum(invalid_ids))

if __name__ == "__main__":
    main()