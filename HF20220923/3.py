def haromszog():
    a = int(input("a oldal (cm):"))
    b = int(input("b oldal (cm):"))
    c = int(input("c oldal (cm):"))
    if ((a < b + c) and (b < a + c) and (c < a + b)):
        print("A " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög szerkeszthető.")
    else:
        print("A " + str(a) + ", " + str(b) + " és " + str(c) + " oldalú háromszög NEM szerkeszthető.")

def main():
    haromszog()

if __name__ == "__main__":
	main()