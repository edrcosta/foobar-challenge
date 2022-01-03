def f(a): 
    return [a, 1, a+1, 0][a%4]

def XOR(a, b): 
    return f(b) ^ f(a-1)

def solution(start, length):
    l = length
    result = 0
    while l > 0:
        result^= XOR(start,start+l-1)
        start = start + length
        l = l - 1
    return result

print(solution(17, 4))

#https://stackoverflow.com/questions/10670379/find-xor-of-all-numbers-in-a-given-range
#https://stackoverflow.com/questions/39940954/python-fast-xor-over-range-algorithm/39941113