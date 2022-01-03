def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


# def solution(l):
#     result = []
#     end = len(l)
#     while len(l)> 0:
#         current = l.pop()
        
#         v = current
#         v_arr = v.split(".")
#         v_major = int(v_arr[0])
#         v_rev = int(v_arr[1]) if len(v_arr) >= 2 else 0
#         v_minor = int(v_arr[2]) if len(v_arr) >= 3 else 0

#         for i, vv in enumerate(result):
#             vv_arr = vv.split(".")
#             vv_major = int(vv_arr[0])
#             vv_rev = int(vv_arr[1]) if len(vv_arr) >= 2 else 0
#             vv_minor = int(vv_arr[2]) if len(vv_arr) >= 3 else 0
            
#             is_lower_or_equal = False

#             if vv_major < v_major:
#                 is_lower_or_equal = True
#             else:
#                 if vv_rev < v_rev:
#                     is_lower_or_equal = True
#                 else:
#                     if vv_minor <= v_minor:
#                         is_lower_or_equal = True

            

#             if is_lower_or_equal:
#                 print(vv, "<=", v)
#             # result.insert(0, current)
#             # print(v)


#         if len(result) == 0:
#             result.insert(0, current)
            
#     return result

# result = solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
# print(result)




# # "1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"


