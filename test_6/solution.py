from fractions import Fraction

def get_probabilities(m):
    for row in range(len(m)):
        _sum = sum(m[row])

        if _sum != 0:
            for i in range(len(m[row])):
                m[row][i] /= float(_sum)
    return m

def calculate_r_and_q(m, t_states, nt_states):
    R = []
    Q = []

    for i in nt_states:
        t = []
        n = []
        for j in t_states: t.append(m[i][j])
        for j in nt_states: n.append(m[i][j])
        R.append(t)
        Q.append(n)
    return [R, Q]

def substract_q_from_identity(Q):
    for row in range(len(Q)):
        for item in range(len(Q[row])):
            if row != item:Q[row][item] = -Q[row][item]
            else : Q[row][item] = 1 - Q[row][item]
    return Q

def minor_matrix(Q,i,j):
    min_matrix = []
    for row in Q[:i] + Q[i+1:]:
        temp = []
        for item in row[:j] + row[j+1:]:
            temp.append(item)
        min_matrix.append(temp)
    return min_matrix

def determinant_of(Q):
    determinant = 0

    if len(Q) == 1: return Q[0][0]
    elif len(Q) == 2: return Q[0][0]*Q[1][1] - Q[0][1]*Q[1][0]
    
    for first in range(len(Q[0])):
        min_matrix = minor_matrix(Q, 0, first)
        determinant += (((-1)**first)*Q[0][first] * determinant_of(min_matrix))

    return determinant

def transpose_matrix_square(matrix):
    for y in range(len(matrix)):
        for x in range(y, len(matrix), 1):
            matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
    return matrix

def invert_matrix(Q):
    Q1 = []
    for row in range(len(Q)):
        res = []
        for column in range(len(Q[row])):
            min_matrix = minor_matrix(Q, row, column)
            determinant = determinant_of(min_matrix)
            res.append(((-1)**(row+column))*determinant)
        Q1.append(res)
    
    determinant = determinant_of(Q)
    Q1 = transpose_matrix_square(Q1)

    for i in range(len(Q)):
        for j in range(len(Q[i])):
            Q1[i][j] /= float(determinant)
    return Q1

def multiply_matrix(A, B):
    result = []
    dimension = len(A)
    for row in range(len(A)):
        temp = []
        for column in range(len(B[0])):
            product = 0
            for selector in range(dimension):
                product += (A[row][selector]*B[selector][column])
            temp.append(product)
        result.append(temp)
    return result

def map_states(m):
    response = [[], []]

    for row in range(len(m)):
        count = 0
        for item in range(len(m[row])):
            if m[row][item] == 0: count += 1

        response[0 if count == len(m) else 1        ].append(row)
    return response

def solution(m):
    if len(m) == 1 and len(m[0]) == 1 and m[0][0] == 0: return [1, 1]

    states = map_states(m)
    probabilities = get_probabilities(m)
    rq = calculate_r_and_q(probabilities, states[0], states[1])
    IQ = substract_q_from_identity(rq[1])
    IQ1 = invert_matrix(IQ)
    M = multiply_matrix(IQ1, rq[0])
    
    gcd = lambda a, b: a if b==0 else gcd(b,a%b)

    fraction = [Fraction(i).limit_denominator() for i in M[0]]
    
    lcm = 1
    for i in fraction:
        if i.denominator != 1: lcm = i.denominator
    for i in fraction:
        if i.denominator != 1: lcm = lcm*i.denominator/gcd(lcm, i.denominator)
    
    fraction = [(i*lcm).numerator for i in fraction]
    fraction.append(lcm)
    return fraction

res = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])

print(res)