def solution(message: str, width: int, mode: str):
    chars = [c for c in message if c.isalnum()]
    n = len(chars)
    if n == 0:
        return message
    rows = -(-n // width)     
    remainder = n % width       
    def valid(r, c):
        if remainder == 0 or r < rows - 1:
            return c < width
        else:
            return c < remainder

    row_major_order = [(r, c) for r in range(rows) for c in range(width) if valid(r, c)]
    col_major_order = [(r, c) for c in range(width) for r in range(rows) if valid(r, c)]

    grid = {}
    if mode == "encrypt":
        for i, cell in enumerate(row_major_order):
            grid[cell] = chars[i]
        result_seq = [grid[cell] for cell in col_major_order]
    elif mode == "decrypt":
        for i, cell in enumerate(col_major_order):
            grid[cell] = chars[i]
        result_seq = [grid[cell] for cell in row_major_order]
    else:
        raise ValueError("mode doit être 'encrypt' ou 'decrypt'")
    result = []
    idx = 0
    for c in message:
        if c.isalnum():
            result.append(result_seq[idx])
            idx += 1
        else:
            result.append(c)
    return "".join(result)