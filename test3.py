import re

# def solution(chaine: str):
#     element = re.split(r"0+",chaine)
#     return {"first_name": element[0], "id" : element[2], "last_name" : element[1]}

    
# def solution(chaine: str) -> dict:
#     parts = []
#     current = ""
#     for c in chaine:
#         if c == '0':
#             if current:
#                 parts.append(current)
#                 current = ""
#         else:
#             current += c
#     if current:
#         parts.append(current)

#     return {"first_name": parts[0], "last_name": parts[1], "id": parts[2]}

def solution(chaine: str):
    partie = [p for p in chaine.replace("0"," ").split() ]
    return {"first_name": partie[0], "last_name": partie[1], "id": partie[2]}

def solution(chaine: str):
    parts = []
    current = ""
    for c in chaine:
        if c == '0':
            if current:
                parts.append(current)
                current = ""
        else:
            current += c
    if current:
        parts.append(current)
    if len(parts) != 3:
        return None 
    first_name, last_name, id_ = parts
    return {"first_name": first_name, "last_name": last_name, "id": id_}

print(solution("John000Doe000123"))
print(solution("Kocou00000Elom000125"))