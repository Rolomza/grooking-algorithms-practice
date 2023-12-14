# Binary search O(log n)
# It runs in logarithmic time.

# If I want to do a simple search, it would be O(n). Linear time. DO NOT DO THIS!

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]


print(binary_search(my_list,3))
print(7 // 2)