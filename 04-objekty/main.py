import datetime
import random
mena = ["Jano", "Roman", "Sebastián", "Rudo", "Samuel"]
priezviska = ["Trulo", "Dangl", "Ostrý", "Krehký", "Tvrdý"]
class Osoba:
    def __init__(self, meno, priezvisko, rok):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok
    def pozdrav(self):
        print(f"Ahoj, ja som {self.meno} {self.priezvisko} a mám {self.vek} rokov")
class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok)
        self.trieda = trieda
    def pozdrav(self):
        Osoba.pozdrav(self)
        print(f"Som študent {self.trieda} triedy")
class Ucitel(Osoba):
    def __init__(self, meno, priezvisko, rok, titul="", trieda=""):
        super().__init__(meno, priezvisko, rok)
        self.titul = titul
        self.trieda = trieda
    def pozdrav(self):
        print(f"Dobrý deň, volám sa {self.titul} {self.meno} {self.priezvisko} a mám {self.vek} rokov.")
        if self.trieda != "":
            print(f"Som tridny učiteľ {self.trieda} triede")
jano = Osoba("Ján", "Mrkvička", 2006)
jano.pozdrav()
fero = Osoba("Fero", "Mravec", 2000)
fero.pozdrav()
ondrej = Student("Ondrej", "Šarlina", 2007, "III.AT")
ondrej.pozdrav()
sutek = Ucitel("Michal", "Šutek", 1978, "Mgr.", "III.AT")
sutek.pozdrav()
palica = Ucitel("Michal", "Palica", 1985, "Mgr.")
palica.pozdrav()
for i in range(5):
    a = random.randint(0, len(mena) - 1)
    b = random.randint(0, len(priezviska) - 1)
    rok_ucitel = random.randint(1975, 1990)
    ucitel1 = Ucitel(mena[a], priezviska[b], rok_ucitel)
    ucitel1.pozdrav()
for i in range(5):
    a = random.randint(0, len(mena) - 1)
    b = random.randint(0, len(priezviska) - 1)
    c = random.randint(1,4)
    rok_student = random.randint(2005, 2010)
    student1 = Student(mena[a], priezviska[b], rok_student , f"trieda {c}.")
    student1.pozdrav()
#du mena 5 učitelou a žiakov s náhodnými menami a uloží ich do pola 