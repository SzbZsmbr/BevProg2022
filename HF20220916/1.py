#!/usr/bin/env python
# coding: utf8
def gyakorisag(mondat):
    dict = {}
    for x in mondat:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] = dict[x]+1 
    print("Betűk gyakorisága:" + str(dict))

def main():
    print("Adjon meg egy mondatot:")
    mondat = input()
    gyakorisag(mondat)
    print(mondat[::-1])
    print(mondat.split(" "))
    



        

if __name__ == "__main__":
	main()