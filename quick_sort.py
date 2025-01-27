def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(list1, start, end):
    pivot = swap_index = start
    for i in range(start+1, end+1):
        if list1[i] < list1[pivot]:
            swap_index += 1
            swap(list1, i, swap_index)
    swap(list1, pivot, swap_index)
    return swap_index

# for almost sorted or sorted data O(n^2), insertion sort is better
def __quick_sort(list1, start, end):
    if start > end:
        return my_list
    pivot_index = pivot(list1, start, end) 
    __quick_sort(list1, start, pivot_index-1)
    __quick_sort(list1, pivot_index+1, end)


def quick_sort(list1):
    return __quick_sort(list1, 0, len(list1)-1)




my_list = [4,6,1,7,3,2,5]

quick_sort(my_list)

print(my_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7]
    
 """



"""
    EXPECTED OUTPUT:
    ----------------
    List before running pivot():
    [4, 6, 1, 7, 3, 2, 5]

    List after running pivot():
    [2, 1, 3, 4, 6, 7, 5]

    Returned Swap Index:
    3

 """