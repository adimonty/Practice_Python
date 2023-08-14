from collections import defaultdict, Counter

def count_names(filename):
    counter_dict = defaultdict(int)  
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            counter_dict[line] += 1
    
    return counter_dict

def main():
    filename = 'nameslist.txt'
    name_counts = count_names(filename)
    
    print(name_counts)

if __name__ == "__main__":
    main()
