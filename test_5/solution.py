def solution(M, F):
    generations = 0 
    M = int(M)
    F = int(F)

    multiplier = lambda a, b: ((a - b) / b) + 1

    while True:
        if M <= 0 or F <= 0: break

        if M <= 100 or F <= 100:
            if M > F: M -= F
            elif F > M: F -= M
            else: break
            generations += 1
        else:
            if M > F:
                MM = multiplier(M, F)
                M -= F * MM
                generations += MM
            elif F > M:
                MM = multiplier(F, M)
                F -= M * MM
                generations += MM
            else: break

    possible = M == 1 and F == 1 and generations >= 0
    return str(generations if possible else 'impossible')


numbers = [
    # ['2000000010', '2000000010', "48101"],
    # ['112323123038374888', '2341553341223', "48101"],
    # ['1123231230382374888', '2341553341223', ""],
    ['4', '7', ""],
]


for n in numbers:
    res = solution(n[0], n[1])
    print(n, res)




# '2', '1'
# 1
# '4', '7'
# 4