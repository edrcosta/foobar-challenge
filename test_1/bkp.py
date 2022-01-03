import time
start_time = time.time()

def solution(s):
    result = ""
    letters = [ "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alphabet = ( 
        "100000", # A 
        "110000", # B
        "100100", # C 
        "100110", # D 
        "100010", # E 
        "110100", # F 
        "110110", # G 
        "110010", # H 
        "010100", # I
        "010110", # J
        "101000", # K
        "111000", # L
        "101100", # M
        "101110", # N
        "101010", # O
        "111100", # P
        "111110", # Q
        "111010", # R
        "011100", # S
        "011110", # T
        "101001", # U
        "111001", # V
        "010111", # W
        "101101", # X
        "101111", # Y
        "101011", # Z
        "100000", # A 
        "100000", # A 
        "100000", # A 
        "100000", # A 
        "100010", # E 
        "100010", # E 
        "100010", # E 
        "100010", # E
        "010100", # I
        "010100", # I
        "010100", # I
        "010100", # I
        "101010", # O
        "101010", # O
        "101010", # O
        "101010", # O
        "101001", # U
        "101001", # U
        "101001", # U
        "101001", # U 
        "100100", # C 
    )

    single_word_cap_mark = '*'
    
    # clear all left and right spaces
    s = s.strip()
    if len(s) == 0:
        return '000000'

    uppercase_all_letters = s.isupper() and len(s) > 2

    # capitalization mark 
    if uppercase_all_letters:
        result = "000011"

    # run by chars
    for character in list(s):
        if character == " ":
            result = result + "000000"
        elif character.upper() not in letters:
            continue
        else:
            if character.isupper() and not uppercase_all_letters:
                result += single_word_cap_mark
            result += alphabet[letters.index(character.upper())]
    
    # replace simbols to the proper capitalizaztion marks 
    if not uppercase_all_letters:
        result = result.replace("000000*", "000001").replace("000001*", "000001")
    result = result.replace("*", "000001")

    return result



# =================== testing

words = [
    ["code", "100100101010100110100010"],
    ["Braille", "000001110000111010100000010100111000111000100010"],
    ["The quick brown fox jumps over the lazy dog","000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"],
    ["   A", "000000000000000001100000", "000001100000"],
    [" AaAa ", "000001100000100000000001100000100000"],
    [" AAA ", "000011100000100000100000"],
    [" AAB ", "000011100000100000110000"],
    [" AAB  a", "000001100000000001100000000001110000000000000000100000"], # @todo join zeros
    [" aaa AAA a", "100000100000100000000001100000000001100000000001100000000000100000"], # @todo join zeros
    ["àààÀ", '100000100000100000000001100000']
]

for test in words:
    if len(test) > 2:
        print(solution(test[0]) == test[1] or solution(test[0]) == test[2], solution(test[0]))
    else:
        print(solution(test[0]) == test[1], solution(test[0]))



print("--- %s seconds ---" % (time.time() - start_time ))
