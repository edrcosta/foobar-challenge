def solution(l):
    for i in range(len(l)):
        for ii in range(i):
            
            if ii+1 > len(l) -1: continue

            v = l[ii]
            v = v.split(".")
            v_major = int(v[0])
            v_rev = int(v[1]) if len(v) >= 2 else 0
            v_minor = int(v[2]) if len(v) >= 3 else 0

            vv = l[ii+1]
            vv = vv.split(".")
            vv_major = int(vv[0])
            vv_rev = int(vv[1]) if len(vv) >= 2 else 0
            vv_minor = int(vv[2]) if len(vv) >= 3 else 0

            need_swap = False
            if v_major > vv_major:
                need_swap = True
            elif v_major == vv_major and v_rev > vv_rev:
                need_swap = True
            elif v_rev == vv_rev and v_minor > vv_minor:
                need_swap = True

            if v_rev == 0 and vv_rev == 0 and v_minor == 0 and vv_minor == 0:
                if v_major == vv_major and len(vv) <= len(v):
                    need_swap = True

            if need_swap:
                l[ii], l[ii + 1] = l[ii+1], l[ii]            

    return l

result = solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
print("result", result)
