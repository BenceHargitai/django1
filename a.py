from os import truncate


lista = []

with open("input.txt","r", encoding="utf8") as f:
    for szam in f:
        lista.append(int(szam))
    

# 3.000-D
# Olvassuk be az alábbi fájl tartalmmát egy listába/tömbbe,
# majd a következő feladatokat oldjuk meg.
# Minden feladat előtt a program írja ki a feladat sorszámát!
# 1. Mennyi a sorozatban található számok szorzata?
# 2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!
index = 0
for elem in lista:
    elem=elem+1
    if elem%5==0 or elem%7==0:
        index = elem
print(elem)


# 3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!
# 4. Igaz-e, hogy minden szám negatív?
index = 0
for elem in lista:
    if elem>0:
        index = 1

print('igen' if index==0 else 'nem igaz')
    
    
# 5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?
# 6. Hány 18-cal osztható szám található a sorozatban?
index = 0
for elem in lista:
    if elem%18==0:
        index = index+1
print(index)
# 7. Mennyi a sorozatban található egyik legkisebb szám indexe?
# 8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!

for elem in lista:
    if elem%17==0 or elem%18==0:
        print(elem*elem)
# 9. Hány eleme van a sorozatnak?
# 10. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?

jobb = False
kozepso = False
megvan = False
for elem in lista:
    print(elem)
    if (elem%2==0):
        jobb=True

    if(elem%2!=0 and jobb==True):
        kozepso=True

    if (jobb==True and kozepso==True and elem%2==0):
        megvan = True
        print('megvan')
        break
    if (jobb==True and kozepso==True and elem%2!=0):
        jobb, kozepso == False

print('van' if megvan==True else 'nincs ilyen')