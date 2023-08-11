def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def main():
    ordered_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target_number = int(input("Enter a number to check: "))
    
    found = binary_search(ordered_list, target_number)
    
    if found:
        print(f"{target_number} is in the list.")
    else:
        print(f"{target_number} is not in the list.")

if __name__ == "__main__":
    main()
