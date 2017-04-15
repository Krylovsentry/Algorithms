# O(n ** 2)
def bubble_sort(slist, asc=True):
    need_exchanges = False
    for iteration in range(len(slist))[:: -1]:
        for j in range(iteration):
            if asc:
                if slist[j] > slist[j + 1]:
                    need_exchanges = True
                    slist[j], slist[j + 1] = slist[j + 1], slist[j]
            else:
                if slist[j] < slist[j + 1]:
                    need_exchanges = True
                    slist[j], slist[j + 1] = slist[j + 1], slist[j]
        if not need_exchanges:
            return slist
    return slist


print(bubble_sort([8, 1, 13, 34, 5, 2, 21, 3, 1], False))
print(bubble_sort([1, 2, 3, 4, 5, 6]))
