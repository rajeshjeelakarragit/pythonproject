def kthsmallest(list, k):
    sorted_list = sorted(list)
    return sorted_list[k - 1]


list = [3, 12, 10, 5, 12, 11]

k = 3
minNum = kthsmallest(list, k)
print(minNum)