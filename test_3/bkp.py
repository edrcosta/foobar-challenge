def solution(l):
    result = l.copy()

    for i, v in enumerate(l):
        # useful types
        v_str = v
        v_arr = v.split(".")
        
        # get version parts 
        major_v = float(v_arr[0])
        minor_v = "0"
        revis_v = "0"
        
        # optional version parts
        if len(v_arr) >= 2:
            revis_v = v_arr[1]
        if len(v_arr) == 3:
            minor_v = v_arr[2]
        rev_minor_v = float(revis_v + "." + minor_v)        

        print(">> ", v_str, '     MAJOR', major_v, "    rev_minor", rev_minor_v)

        loop_count = 0
        while loop_count < len(l):
            # skip current number
            if i == loop_count:
                loop_count+=1
                continue

            # useful types
            vv = result[loop_count]
            vv_str = vv
            vv_arr = vv.split(".")

            # get version parts 
            major_vv = float(vv_arr[0])
            minor_vv = "0"
            revis_vv = "0"

            # optional version parts
            if len(vv_arr) >= 2:
                revis_vv = vv_arr[1]
            if len(vv_arr) == 3:
                minor_vv = vv_arr[2]

            # convert to float
            rev_minor_vv = float(revis_vv + "." + minor_vv)        
    
    
            print("CHECK ", vv_str, '     MAJOR', major_vv, "    rev_minor", rev_minor_vv)

            # check if is a lower elevator version

            is_lower_or_equal = False
            if major_v > major_vv:
                is_lower_or_equal = True
            else :
                if revis_v > revis_vv:
                    
                    is_lower_or_equal = True
                else:
                    if minor_vv <= minor_v:
                        is_lower_or_equal = True
             



            if major_v == major_vv and rev_minor_v == rev_minor_vv:
                if len(result[loop_count]) > len(v_str):
                    is_lower_or_equal = False

            not_aready_moved = result.index(v_str) < loop_count

            if is_lower_or_equal and not_aready_moved:
                # Move number left <<<<
                index = result.index(v_str) 
                value = result[loop_count]
                del result[loop_count]

                # prevent array index error
                if index < 0:
                    index = 0

                # adds back 
                result.insert(index, value)
            loop_count+=1 # increment loop 
    return ",".join(result)


result = solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
print("result", result)


# # 1.0.2 <= 1.0.12
# # 
# major_v = 1
# revis_v = 0
# minor_v = 2

# major_vv = 1
# revis_vv = 0
# minor_vv = 3

# is_lower_or_equal = False
# if major_v > major_vv:
#     is_lower_or_equal = True
# else :
#     if revis_v > revis_vv:
        
#         is_lower_or_equal = True
#     else:
#         if minor_vv <= minor_v:
#             is_lower_or_equal = True

# print(is_lower_or_equal)