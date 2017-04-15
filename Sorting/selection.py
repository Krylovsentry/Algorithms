# O(n ** 2)
def selection_sort(alist):
    for i in range(len(alist))[::-1]:
        position_of_max = 0
        for j in range(i + 1):
            if alist[j] > alist[position_of_max]:
                position_of_max = j
        alist[i], alist[position_of_max] = alist[position_of_max], alist[i]
    return alist

print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([1, 3, 8, 5, 11, 22, 3, 9]))