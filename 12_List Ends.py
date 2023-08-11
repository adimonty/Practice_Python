def extract_first_and_last(input_list):
    if len(input_list) < 2:
        return "List must have at least two elements"
    
    result = [input_list[0], input_list[-1]]
    return result