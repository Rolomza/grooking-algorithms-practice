def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_pos = findSmallest(arr)
        newArr.append(arr.pop(smallest_pos))
    return newArr

print(selection_sort([55,6,2,1,87,3,4]))