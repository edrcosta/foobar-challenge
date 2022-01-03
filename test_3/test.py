def convert(a):
    aa = a.split(".")
    return [int(aa[0]), int(aa[1] if len(aa) >= 2 else "0"), int(aa[2] if len(aa) >= 3 else "0")]

def is_bigger(a, b):
    aa = convert(a)
    bb = convert(b)

    if aa[0] > bb[0]:
        return True
    elif aa[0] == bb[0] and aa[1] > bb[1]:
        return True
    elif aa[1] == bb[1] and aa[2] > bb[2]:
        return True
    if (aa[1] == 0 and bb[1] == 0 and aa[2] == 0 and bb[2] == 0) and (aa[0] == bb[0] and len(b) <= len(a)):
        return True
    return False

def solution(l):
    # n
    parts = [0]
    cut = 0
    for i in range(0, len(l)):
        if cut == 1:
            cut = 0
            parts.append(i)
        cut +=1

    # n / 2
    result = []
    parts_re = []
    while not len( parts) == 0:
        
        if len(parts) == 0: continue
        left = parts[0]
        del parts[0]
    
        if len(parts) == 0:
            result = left
            continue
        rigth = parts[0]
        del parts[0]

        part = [l[left], l[rigth]]
        if is_bigger(part[0], part[1]): 
            part[0], part[1] = part[1], part[0]

        parts_re.append(part)


    print(parts_re)

    return result

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0", "2.0.0", "2.0", "2.0"]))
# # start = 0
# # mid = len(l) / 2
# # end = len(l)

# # print(start, mid, end)


# # start = start / 2
# # mid = mid / 2
# # end = end / 2

# # print(start, mid, end)

# # direita 
# start = len(l) / 2
# end = len(l)
# mid = end - start / 2

# print(start, mid, end)








# while not done:







#     if control > 10:
#         done = True
#     control+=1



