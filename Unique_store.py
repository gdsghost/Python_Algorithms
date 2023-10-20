# unique_elements_advanced.py

def unique_elements_advanced(arr):
    unique_dict = {}
    unique_list = []

    for element in arr:
        if element not in unique_dict:
            unique_dict[element] = True
            unique_list.append(element)

    return unique_list

if __name__ == "__main__":
    # Example usage:
    my_array = [1, 2, 2, 3, 4, 4, 5]
    unique_elements_list = unique_elements_advanced(my_array)
    print(unique_elements_list)
