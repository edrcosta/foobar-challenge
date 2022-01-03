def solution(l):
    if len(l) == 1:
        return l

    center = int(len(l)/2)
    left = l[0:center]
    rigth = l[center:len(l)]

    solution(left)
    solution(rigth)

    i = 0
    ii = 0
    iii = 0

    while i < len(left) and ii < len(rigth):

        a_arr = left[i].split(".")
        if len(a_arr) == 3:
            if int(a_arr[2]) < 10:
                aa = float(a_arr[0] + "." + a_arr[1] + "0" + a_arr[2])
            else:
                aa = float(a_arr[0] + "." + a_arr[1] + a_arr[2])
        else:
            aa = float(left[i])
        
        b_arr = rigth[ii].split(".")
        if len(b_arr) == 3:
            if int(b_arr[2]) < 10:
                bb = float(b_arr[0] + "." + b_arr[1] + "0" + b_arr[2])
            else:
                bb = float(b_arr[0] + "." + b_arr[1] + b_arr[2])
        else:
            bb = float(rigth[ii])
    
    
        if aa < bb:
            print(aa, bb)
            l[iii] = left[i]
            i += 1
        else:
            l[iii] = rigth[ii]
            ii += 1
        iii += 1

    while ii < len(rigth):
        l[iii] = rigth[ii]
        ii += 1
        iii += 1

    while i < len(left):
        l[iii] = left[i]
        i += 1
        iii += 1
    return ",".join(l)


arr = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
arr = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
print(solution(arr))