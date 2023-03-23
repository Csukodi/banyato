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

def atlagolas(m):
    osszeg=0
    darab=0
    for seged_lista in m:
        for elem in seged_lista:
            if elem>0:
                darab+=1
                osszeg+=elem
    return osszeg/darab



atlagos_melyseg=0

print(f"A tó felszíne: {megszamolas(melysegek)*1} m2, átlagos mélysége: {atlagolas(melysegek)/10:0.2f} m")


print("4. feladat")

def max_kivalasztas(m):
    max_sor=0
    max_oszlop=0
    for i in range(1,len(m)):
        for j in range(len(m[i])):
            if m[max_sor][max_oszlop]<m[i][j]:
                max_oszlop=i
                max_sor=j
    return max_sor,max_oszlop
        

max_s, max_o=max_kivalasztas(melysegek)

print(f"A tó legnagyobb mélysége: {melysegek[max_s][max_o]} dm")

print("A legmélyebb helyek sor-oszlop koordinátái:")

def legmelyebb_pontok_koordinatai(m, max):
    for sor_index,sor in enumerate(m):
        for oszlop_index,elem in enumerate(sor):
            if elem==max:
                print(f"{sor_index+1};{oszlop_index+1}", end=" ")
    print()

# print("(14; 20) (26; 11) (32; 16)")
legmelyebb_pontok_koordinatai(melysegek, melysegek[max_s][max_o])


def partvonal_hossza(m):
    hossz=0
    for i in range(1, len(m)-1):
        for j in range(1, len(m[i])-1):
            if m[i][j]>0:
                if m[i-1][j]==0:
                    hossz+=1
                if m[i+1][j]==0:
                    hossz+=1
                if m[i][j-1]==0:
                    hossz+=1
                if m[i][j+1]==0:
                    hossz+=1
    return hossz


print("5. feladat")
print(f"A tó partvonala {partvonal_hossza(melysegek)} m hosszú")



print("6. feladat")
be_oszlop=int(input("A vizsgált szelvény oszlopának azonosítója=") or "6")-1

with open("diagram.txt","w",encoding="utf-8") as fout:
    for sor_index, sor in enumerate(melysegek):
        print(f"{sor_index+1:2d}","*"*sor[be_oszlop], file=fout)