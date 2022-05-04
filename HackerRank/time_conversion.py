def timeConversion(s):
    list = []
    for _ in s:
        list.append(_)
    if s[8:] == "AM":
        list.remove("A")
        list.remove("M")
        if list[0] == "1" and list[1] == "2":
            list[0] = "0"
            list[1] = "0"
        return "".join(list)
        

    else:
        list.remove("P")
        list.remove("M")
        if list[0] == "1" and list[1] == "2":
            return "".join(list)
        else:
            list[0] = str(int(list[0])+1)
            list[1] = str(int(list[1])+2)
            if list[0] == "2" and list[1] == "4":
                list[0] = "0"
                list[1] = "0"
            return "".join(list)
