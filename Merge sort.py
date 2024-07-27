def sort(list):
    length = len(list)
    for i in range(length):
        is_sorted = False
        for j in range(0, length - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                is_sorted = True
        if not is_sorted:
            break

def merge_sort(list):
    length = len(list)
    if length > 1:
        mid = length // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

list = []
while True:
    choice = input('enter a number or quit: ')
    if choice == 'quit':
        break
    else:
        z = int(choice)
        list.append(z)

merge_sort(list)
print(list)
