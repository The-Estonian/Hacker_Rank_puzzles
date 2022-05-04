# def solve(s):
#     list = []
#     counter = 0
#     for _ in s:
#         if _ != " " and counter == 0:
#             list.append(_.capitalize())
#             counter += 1
#         elif _ == " ":
#             counter = 0
#             list.append(_)
#         elif counter == 1:
#             list.append(_)
#     return "".join(list)

def solve(s):
    s = s.split()
    list = []
    for _ in s:
        list.append(_.capitalize())
    
    return " ".join(list)


print(solve("hello   world  lol"))