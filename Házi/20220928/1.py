def hanyados():
    while True:
        try:       
            a = int(input("Enter 'a' value: "))
            b = int(input("Enter 'b' value: "))
            print(a/b)
        except ZeroDivisionError:
            print("Division by zero not allowed")
        print("Out of try blocks")

def main():
    hanyados()


if __name__ == "__main__":
    main()