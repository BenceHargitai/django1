def szorzat(lista):
    szam = 1
    for i in lista:
        szam *= i
    return szam

def harmadik(lista):
    for i in lista:
        if i > 1 and i < 10:
            return True
    return False

def egyiklegkisebb(lista):
    i = 0
    szam = lista[0]
    szam_index = 0
    while i > 0:
        if i < szam:
            szam = lista[i]
            szam_index = i
        i += 1
    return szam_index
    

lista = []

with open("input.txt","r", encoding="utf8") as f:
    for szam in f:
        lista.append(int(szam))
    
print(f'1. Mennyi a sorozatban található számok szorzata? {szorzat(lista)}')
print(f'3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét! {list(filter(lambda x : x%3==0 and x%7 == 0, lista))[0]}')
print(f'5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik? {harmadik(lista)}')
print(f'7. Mennyi a sorozatban található egyik legkisebb szám indexe? {egyiklegkisebb(lista)}')
print(f'9. Hány eleme van a sorozatnak? {len(lista)}')

# 3.000-D
# Olvassuk be az alábbi fájl tartalmmát egy listába/tömbbe,
# majd a következő feladatokat oldjuk meg.
# Minden feladat előtt a program írja ki a feladat sorszámát!
# 1. Mennyi a sorozatban található számok szorzata?
# 2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!
# 3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!
# 4. Igaz-e, hogy minden szám negatív?
# 5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?
# 6. Hány 18-cal osztható szám található a sorozatban?
# 7. Mennyi a sorozatban található egyik legkisebb szám indexe?
# 8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!
# 9. Hány eleme van a sorozatnak?
# 10. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?

