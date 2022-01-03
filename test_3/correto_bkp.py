def convert(a):
    aa = a.split(".")
    return [int(aa[0]), int(aa[1] if len(aa) >= 2 else "0"), int(aa[2] if len(aa) >= 3 else "0")]

cache = {}
def is_bigger(a, b):
    
    if a+"-"+b in cache.keys():
        return cache[a+"-"+b]
    aa = convert(a)
    bb = convert(b)

    response = False
    if aa[0] > bb[0]:
        response = True
    elif aa[0] == bb[0] and aa[1] > bb[1]:
        response = True
    elif aa[1] == bb[1] and aa[2] > bb[2]:
        response = True
    if (aa[1] == 0 and bb[1] == 0 and aa[2] == 0 and bb[2] == 0) and (aa[0] == bb[0] and len(b) <= len(a)):
        response = True
    
    cache[a+"-"+b] = response

    return response

def merge(l):
    if len(l) <= 1: return l

    mid = int(len(l) / 2)
    left = l[:mid]
    right = l[mid:]

    merge(left)
    merge(right)

    i = 0
    ii = 0
    iii = 0
    
    while i < len(left) and ii < len(right):

        if not is_bigger(left[i], right[ii]):
            l[iii] = left[i]
            i += 1
        else:
            l[iii] = right[ii]
            ii += 1
        iii += 1

    while i < len(left):
        

        l[iii] = left[i]
        i += 1
        iii += 1

    while ii < len(right):
        

        l[iii]=right[ii]
        ii += 1
        iii += 1
    return l


# def quick(l): 
#     def sorting(l, start, end):
#         if start >= end: return False
    
#         pivot = l[end]
#         current = start - 1
        
#         for i in range(start, end):
#             if is_bigger(pivot, l[i]):
#                 current = current + 1
#                 l[current], l[i] = l[i], l[current]

#         l[current + 1], l[end] = l[end], l[current + 1]
#         pivot = current + 1

#         sorting(l, start, pivot - 1)
#         sorting(l, pivot + 1, end)

#     sorting(l, 0, len(l) - 1)

#     return l

# def insertionSort(l):
#     for i in range(1, len(l)):
#         key = l[i]
#         ii = i-1
#         while ii >= 0 and is_bigger(l[ii], key):
#                 l[ii + 1] = l[ii]
#                 ii -= 1
#         l[ii + 1] = key
#     return l

def binary_search(arr, val, start, end):
    if start == end:
        return start if is_bigger(arr[start], val) else start+1
  
    if start > end:
        return start
  
    mid = (start+end)/2
    
    if is_bigger(val, arr[mid]):
        return binary_search(arr, val, mid+1, end)
    elif is_bigger(arr[mid], val):
        return binary_search(arr, val, start, mid-1)
    return mid
  
def insertion_sort(l):
    for i in range(1, len(l)):
        j = binary_search(l, l[i], 0, i-1)
        l = l[:j] + [l[i]] + l[j:i] + l[i+1:]
    return l


def solution(l):
    if type([]) == list:
        if all(is_bigger(l[i+1], l[i]) for i in range(len(l)-1)): 
            return l
        return insertion_sort(l)
    return []


# print("Sorted array:")
# print(solution(["1", "2", "3"]))

# print(solution(["2.11", "2.11"]))
print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
# # print(solution(["1", "2.0", "3"]))


 
# Driver code to test above
# arr = [12, 11, 13, 5, 6]
# print(insertionSort(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
    
    