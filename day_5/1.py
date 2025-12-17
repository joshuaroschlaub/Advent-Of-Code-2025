def main():
    fresh_ranges = []
    with open("day_5/input.txt", 'r') as f:
        lines = f.readlines()
        for line in lines[:185]:
            start, end = line.strip().split('-')
            fresh_ranges.append((int(start), int(end)))
    fresh_ranges.sort()
    
    count = 0
    with open("day_5/input.txt", 'r') as f:
        ids = [int(line.strip()) for line in f.readlines()[186:]]
        for id in ids:
            fresh = False
            for fresh_range in fresh_ranges:
                if id >= fresh_range[0] and id <= fresh_range[1]:
                    fresh = True
            if fresh:
                count += 1
    print(count)

if __name__ == "__main__":
    main()