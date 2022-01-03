def solution(l):
    def sorting(l, start, end):
        if start >= end: return False
    
        pivot = l[end]
        current = start - 1
        
        pivot_arr = pivot.split('.')            
        p_major = int(pivot_arr[0])
        p_rev = int(pivot_arr[1]) if len(pivot_arr) >= 2 else 0
        p_minor = int(pivot_arr[2]) if len(pivot_arr) >= 3 else 0
        
        for i in range(start, end):
            current_arr = l[i].split('.')            
            v_major = int(current_arr[0])
            v_rev = int(current_arr[1]) if len(current_arr) >= 2 else 0
            v_minor = int(current_arr[2]) if len(current_arr) >= 3 else 0

            current_lower = False
            if v_major == p_major and v_rev == p_rev and v_minor == p_minor and len(pivot) <= len(l[i]):
                current_lower = False
            elif v_major < p_major:
                current_lower = True
            elif v_major == p_major and v_rev < p_rev:
                current_lower = True
            elif v_rev == p_rev and v_minor <= p_minor:
                current_lower = True

            if current_lower:
                current = current + 1
                l[current], l[i] = l[i], l[current]

        l[current + 1], l[end] = l[end], l[current + 1]

        pivot = current + 1

        sorting(l, start, pivot - 1)
        sorting(l, pivot + 1, end)

    sorting(l, 0, len(l) - 1)
    
    return ",".join(l)

print(solution(["1.11", "2.0.0", "1.11", "1.2", "2", "0.1","1.11", "1.2.1", "1.1.1", "2.0"]))
# print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))




    

# # print(convert("1.1.2") > convert("1.11"))
# # 

# # -- Python cases --
# # Input:
# # solution.solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
# # Output:
# #     0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0
#     #   0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

# # Input:
# # solution.solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
# # Output:
# #     1.0,1.0.2,1.0.12,1.1.2,1.3.3
#     #   1.0,1.0.2,1.0.12,1.1.2,1.3.3