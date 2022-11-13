import string
with open("hazi.txt", "r", encoding = "UTF-8") as f:
    kimenet = ""
    maganhangzok = "aáeéiíoóöőuüű "
    sor = f.readline()
    i = 1
    while sor:
        if i == 3:
            for x in sor:
                if x not in string.punctuation and x not in maganhangzok:
                    kimenet += x
            i = 0
        sor = f.readline()
        i += 1
    print(kimenet)