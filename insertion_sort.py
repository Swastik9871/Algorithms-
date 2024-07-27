def insertion_sort(list):
    left=0
    right=None
    if right is None:
        right = len(list) - 1

    for i in range(left + 1, right + 1):
        key_item = list[i]
        j = i - 1
        while j >= left and list[j] > key_item:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key_item

    return list

# Example usage:
my_list = [5, 2, 9, 1, 5, 6, 3]
sorted_list = insertion_sort(my_list)
print(sorted_list)