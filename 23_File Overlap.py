def read_numbers_from_file(filename):
    numbers = set()
    with open(filename) as f:
        for line in f:
            numbers.add(int(line.strip()))
    return numbers

def find_overlapping_numbers(file1, file2):
    prime_numbers = read_numbers_from_file(file1)
    happy_numbers = read_numbers_from_file(file2)
    
    overlapping_numbers = prime_numbers.intersection(happy_numbers)
    
    return overlapping_numbers

def main():
    prime_file = "primenumbers.txt"
    happy_file = "happynumbers.txt"
    
    overlapping_numbers = find_overlapping_numbers(prime_file, happy_file)
    
    print("Overlapping numbers:", overlapping_numbers)

if __name__ == "__main__":
    main()