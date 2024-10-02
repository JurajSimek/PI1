print("Zadaj prvé čislo:")
a = int(input())
print("Zadaj druhé číslo")
b = int(input())

def scitanie(a,b):
    c = a+b 
    print("sčitanie", c)

def odcitanie(a,b):
    if(a > b):
        d = a - b 
    if(a < b):
        d = b - a 
    print("odčitanie", d)

def deleno(a,b):
    e = a/b 
    print ("deleno", round(e, 2))

def nasobenie(a,b):
    f = a*b 
    print("nasobenie", f)

scitanie(a,b)
odcitanie(a,b)
deleno(a,b)
nasobenie(a,b)

if(a % 2 == 0):  #párnosť 
    print("Čislo a je párne")
else:
    print("Čislo a je nepáre")

if(b % 2 == 0):
    print("Čislo b je párne")
else:
    print("Čislo b je nepáre")