import random

import time
def binarySearch(ls, value, start, end):
    if start == end:  # If the starting value equals the end value
        if ls[start] > value:
            return start  # If the starting value is greater than value, value will be put in the place of start
        else:
            return start + 1  # The starting value is less than value and will remain in its place

    if start > end:
        return start

    middle = (start + end) // 2  # Calculate the middle position as the average of start and end

    if value < ls[middle]:  # If the value is less than the value in the middle position
        # Runs binary search again, but changes end to middle - 1, checking the next element
        return binarySearch(ls, value, start, middle - 1)
    elif value > ls[middle]:  # If value is larger than the middle value
        # Runs binary search with start value middle + 1
        return binarySearch(ls, value, middle + 1, end)
    else:  # If value is equal to the middle value, the value should be placed in the middle position
        return middle


def bSort(ls):
    length = len(ls)
    for i in range(1, length):
        value = ls[i]
        j = binarySearch(ls, value, 0, i-1)
        popValue = ls.pop(i)
        ls.insert(j, popValue)
    return ls

l = random.sample(range(1,1000000), 100000)
start_time = time.time()
s = bSort(l)
end_time = time.time()
deltatime = end_time - start_time
print(deltatime)