# Function using loop and constructing a new list
def remove_duplicates_loop(input_list):
    unique_list = []
    
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Function using sets
def remove_duplicates_set(input_list):
    return list(set(input_list))

# Example list with duplicates
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# Call the functions and print the results
new_list_loop = remove_duplicates_loop(original_list)
new_list_set = remove_duplicates_set(original_list)

print("Original list:", original_list)
print("New list (using loop):", new_list_loop)
print("New list (using sets):", new_list_set)
