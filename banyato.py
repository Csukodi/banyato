"""
1. feladat
Olvassa be és tárolja el a melyseg.txt állomány adatait, és annak felhasználásával oldja
meg a következő feladatokat! 
"""


melysegek=[]

with open("melyseg.txt","r",encoding="utf-8") as fin:
    fin.readline()
    fin.readline()
    for sor in fin:
        seged_lista=list(map(int,sor.strip().split()))
        melysegek.append(seged_lista)

from colorama import Fore, Back


for melyseg_sor in melysegek:
    for melyseg in melyseg_sor:
        if melyseg>0:
            print(f"{Back.BLUE}{Fore.WHITE}{melyseg:2d}", end=" ")
        else:
            print(f"{Back.RESET}{Fore.BLACK}{melyseg:2d}", end=" ")
    print()

print("2. feladat")
be_sor=int(input("A mérés sorának azonosítója= ") or "12")
be_oszlop=int(input("A mérés oszlopának azonosítója= ") or "6")
be_melyseg=input(f"A mért mélység az adott helyen {melysegek[be_sor-1][be_oszlop-1]} dm")

print("3. feladat")

def megszamolas(m):
    darab=0
    for seged_lista in m:
        for elem in seged_lista:
            if elem>0:
                darab+=1
    return darab


atlagos_melyseg=0

print(f"A tó felszíne: {megszamolas(melysegek)*1} m2, átlagos mélysége: {atlagos_melyseg} m")
