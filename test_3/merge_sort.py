# def convert(a):
#     aa = a.split(".")
#     if not aa[0].isdigit():
#         aa[0] = "0"
#     if len(aa) == 2 and not aa[1].isdigit():
#         aa[1] = "0"
#     if len(aa) == 3 and not aa[2].isdigit():
#         aa[2] = "0"
#     return [int(aa[0]), int(aa[1] if len(aa) >= 2 else "0"), int(aa[2] if len(aa) >= 3 else "0")]

# def is_bigger(a, b):
#     aa = convert(a)
#     bb = convert(b)

#     response = False
#     if aa[0] > bb[0]:
#         response = True
#     elif aa[0] == bb[0] and aa[1] > bb[1]:
#         response = True
#     elif aa[1] == bb[1] and aa[2] > bb[2]:
#         response = True
#     if (aa[1] == 0 and bb[1] == 0 and aa[2] == 0 and bb[2] == 0) and (aa[0] == bb[0] and len(b) <= len(a)):
#         response = True

#     return response

# def binary_search(arr, val, start, end):
#     if start == end:
#         return start if is_bigger(arr[start], val) else start+1
  
#     if start > end:
#         return start
  
#     mid = (start+end)/2
    
#     if is_bigger(val, arr[mid]):
#         return binary_search(arr, val, mid+1, end)
#     elif is_bigger(arr[mid], val):
#         return binary_search(arr, val, start, mid-1)
#     return mid

# def insertion_sort(l):
#     l = l[0:100]
#     for i in range(1, len(l)):
#         j = binary_search(l, l[i], 0, i-1)
#         l = l[:j] + [l[i]] + l[j:i] + l[i+1:]
#     return l


# def solution(l):
#     return insertion_sort(l)


def solution(l):
    l.sort(key=lambda v: map(int, v.split('.')))
    return l


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
# print(solution(data))
