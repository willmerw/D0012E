import random

import time
# returns which pos the element should be placed in in the list

def binary_search(elem, sorted_list, start, end):
    if start == end:
        if elem < sorted_list[start]:
            return start
        else:
            return start + 1
    middle = (start + end)//2
    compare = sorted_list[middle]

    if start > end:
        return start

    if elem < compare:
        return binary_search(elem, sorted_list, start, middle-1)

    if elem > compare:
        return binary_search(elem, sorted_list, middle+1, end)
    else:
        return middle


def bSort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        pos = binary_search(key, ls, 0, i - 1)
        ls.pop(i)
        ls.insert(pos, key)
    return ls

def insertionsort(l):
    for i in range(1,len(l)):
        e = l[i]
        s = i-1
        while e < l[s] and s >= 0:
            l[s + 1] = l[s]
            s = s - 1
        l[s+1] = e

    return l

def insertion_merge_sort(ls, k):
    if len(ls) <= k:
        return insertionsort(ls)
    middle = len(ls)//2
    ls1 = ls[:middle]
    ls2 = ls[middle:]
    l = bmerge_sort(ls1, k)
    r = bmerge_sort(ls2, k)
    i = 0
    li = 0
    ri = 0

    while li < len(l) and ri < len(r):
        if l[li] < r[ri]:
            ls[i] = l[li]
            li = li + 1
        else:
            ls[i] = r[ri]
            ri = ri + 1
        i = i + 1

    if li == len(l):
        for x in range(ri,len(r)):
            ls[i] = r[x]
            i = i + 1
    else:
        for x in range(li,len(l)):
            ls[i] = l[x]
            i = i + 1

    return ls

def bmerge_sort(ls, k):
    if len(ls) <= k:
        return bSort(ls)
    middle = len(ls)//2
    ls1 = ls[:middle]
    ls2 = ls[middle:]
    l = bmerge_sort(ls1, k)
    r = bmerge_sort(ls2, k)
    i = 0
    li = 0
    ri = 0

    while li < len(l) and ri < len(r):
        if l[li] < r[ri]:
            ls[i] = l[li]
            li = li + 1
        else:
            ls[i] = r[ri]
            ri = ri + 1
        i = i + 1

    if li == len(l):
        for x in range(ri,len(r)):
            ls[i] = r[x]
            i = i + 1
    elif ri == len(r):
        for x in range(li,len(l)):
            ls[i] = l[x]
            i = i + 1

    return ls






l = random.sample(range(1,10000000), 1000000)
listan = [1, 10, 4, 5, 13, 12]
start_time = time.time()
print(insertion_merge_sort(l,4))
end_time = time.time()
deltatime = end_time - start_time
print(deltatime)
