
def solution(banana_list):
    loop_tolerance = 1000
    infinite_loops = 0

    for a, ba_a in enumerate(banana_list):
        
        for b, ba_b in enumerate(banana_list):
            
            if a == b: continue 


            loop_counter = 0

            print('>>', ba_a, ba_b)
            while True:
                loop_counter+=1
                if ba_a < ba_b:
                    ba_b-=ba_a
                    ba_a+=ba_a
                    print('A Win', ba_a, ba_b)
                else:
                    ba_a-=ba_b
                    ba_b+=ba_b
                    print('B Win', ba_a, ba_b)
                

                if ba_a != ba_b and ba_b > 0 and ba_a > 0:
                    print('end game\n')

                if loop_counter == loop_tolerance:
                    infinite_loops+=1
                    break
            
            

    print('found', infinite_loops)
    return infinite_loops



solution([1, 7, 3, 21, 13, 19])

