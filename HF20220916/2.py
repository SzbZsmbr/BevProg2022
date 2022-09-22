#!/usr/bin/env python
# coding: utf8

def convert(szam, mertekegyseg):
    if mertekegyseg != "cm" and mertekegyseg != "inch":
        print("Not correct unit!")
    elif mertekegyseg == "cm":
        kiiras = "{} inches"
        print(kiiras.format(szam * 0.3937))
    else:
        kiiras = "{} centimeters"
        print(kiiras.format(szam * 2.54))

def main():
    print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
    szam = float(input())
    mertekegyseg = input()
    convert(szam, mertekegyseg)

if __name__ == "__main__":
	main()