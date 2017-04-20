def find_missing(list1, list2):
    if len(list1 + list2) == 0:
        return 0 

    diff = list(set(list1).difference(set(list2)))
    if len(diff) == 0:
        diff = list(set(list2).difference(set(list1)))
    if len(diff) != 0:
        return diff[0]
    else:
        return 0

print(find_missing([], []))
print(find_missing([7], [7]))
print(find_missing([4, 6, 8], [4, 6, 8, 10]))
