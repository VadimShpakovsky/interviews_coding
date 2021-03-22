RIDDLE_MARK = '?'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
FIRST_LETTER = ALPHABET[0]
LAST_LETTER = ALPHABET[-1]


def next_char(c):
    if c == LAST_LETTER:
        return FIRST_LETTER
    else:
        shift = ord(c) - ord(FIRST_LETTER)

        return ALPHABET[shift + 1]


def solution(riddle):
    answer = ""
    for curr_pos, c in enumerate(riddle):
        if c == RIDDLE_MARK:
            prev = answer[-1] if answer else None
            next = riddle[curr_pos + 1] if curr_pos < len(riddle) - 1 else None

            c = next_char(prev) if prev else FIRST_LETTER
            if c == next:
                c = next_char(next)

        answer += c

    return answer
