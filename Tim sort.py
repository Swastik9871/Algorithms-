def insertion_sort(list, left=0, right=None):
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

def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])

def tim_sort(list):
    min_run = 32
    n = len(list)

    for i in range(0, n, min_run):
        insertion_sort(list, i, min((i + min_run - 1), (n - 1)))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_list = merge(list[start:mid + 1], list[mid + 1:end + 1])
            list[start:start + len(merged_list)] = merged_list

        size *= 2

    return list

# Example usage:
my_list = [5, 2, 9, 1, 5, 6, 3]
sorted_list = tim_sort(my_list)
print(sorted_list)