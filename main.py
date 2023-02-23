S = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
C = "Gmail"
def solution(S, C):
    list_of_names = []
    odp = ""
    list = S.split("; ")
    z = len(list)
    for kek, names in enumerate(list):
        x = names.split(" ")
        x[0] = x[0].lower()
        x[-1] = x[-1].lower()
        if x[-1].count("-") >= 1:
            myslinik = x[-1].find("-")
            x[-1] = x[-1][0:myslinik] + x[-1][myslinik+1:]

        if len(x[-1]) > 8:
            x[-1] = x[-1][0:8]

        index = 0
        for i in list_of_names:
            if i == f"{x[0]}.{x[-1]}@{C}.com":
                index += 1

        list_of_names.append(f"{x[0]}.{x[-1]}@{C}.com")

        if z-1 != kek:
            if index >= 1:
                odp = odp + f"{x[0]}.{x[-1]}{index+1}@{C}.com; "
            else:
                odp = odp + f"{x[0]}.{x[-1]}@{C}.com; "
        else:
            if index >= 1:
                odp = odp + f"{x[0]}.{x[-1]}{index+1}@{C}.com"
            else:
                odp = odp + f"{x[0]}.{x[-1]}@{C}.com"
    return odp

print(solution(S,C))






