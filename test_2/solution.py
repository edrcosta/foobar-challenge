def solution(s):
    greetings_number = 0
    exclude = [" ", "-"]

    _s = []
    for i, char in enumerate(list(s)):
        if not char in exclude:
          _s.append(char)
    
    s = _s
    for i, char in enumerate(list(s)):
        if char == '>':
            for ii, char2 in enumerate(list(s)):
                if ii > i and char2 == '<':
                    greetings_number+=2
    return greetings_number