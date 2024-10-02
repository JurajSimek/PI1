print("Zadaj body max:")
a = int(input())
print("Zadaj kolko mas bodov")
b = int(input())
c = b/a*100
print ("Mas", round(c, 2) , "%") #round zaokluhli desatinne čislo na dve desatinne miesta 

if c > 90:
    print("Dostavas znamku jedna")
elif c <= 75:
    print("Dostavas znamku dva")
elif c <= 50:
    print("Dostavas znamku tri")
elif c <= 30:
    print("Dostavas znamku štyri")
else:
    print("Dostavas znamku pät")