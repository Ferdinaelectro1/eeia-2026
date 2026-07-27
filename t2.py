def solution(montant: str) -> int:
    s = montant.strip()
    if not s:
        return 0
    i, n = 0, len(s)
    sign = 1
    if s[i] in ('+', '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    start = i
    while i < n and s[i].isdigit():
        i += 1
    if start == i:         
        return 0
    value = sign * int(s[start:i])
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    return max(INT_MIN, min(INT_MAX, value))


print(solution("   20000000000000000000gyf  "))  