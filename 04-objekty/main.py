import datetime
import random

pocet_studentov = 100
pocet_ucitelov = 10


class Osoba:
    def __init__(self, meno, priezvisko, rok):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self):
        print("Ahoj, ja som", self.meno, self.priezvisko, "a mám", self.vek, "rokov")

    def vypis_vek(self):
        print(self.vek)


class Ucitel(Osoba):
    def __init__(self, meno, priezvisko, rok, predmety, trieda="", titul=""):
        Osoba.__init__(self, meno, priezvisko, rok)
        self.titul = titul
        self.predmety = predmety
        self.trieda = trieda

    def vypis_predmety(self):
        print(self.predmety)

    def pozdrav(self):
        print("Ahoj, ja som", self.titul, self.meno, self.priezvisko, "a mám", self.vek, "rokov")
        print("Učím predmety:", self.predmety)
        if self.trieda != "":
            print("Som triedny", self.trieda, "triede")

    def vypis_ziakov(self):
        if self.trieda != "":
            print("Študenti v mojej triede:")
            for i in range(pocet_studentov):
                if studenti[i].trieda == self.trieda:
                    print(studenti[i].meno, studenti[i].priezvisko, studenti[i].vek, studenti[i].trieda)


class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        Osoba.__init__(self, meno, priezvisko, rok)
        self.trieda = trieda

    def vypis_triedny(self):
        for i in range(pocet_ucitelov):
            if ucitelia[i].trieda == self.trieda:
                print("Môj triedny učitel je", ucitelia[i].meno, ucitelia[i].priezvisko)

    def pozdrav(self):
        Osoba.pozdrav(self)
        print("Som študent", self.trieda, "triedy")


with open('mena.txt', "r", encoding="utf-8") as t:
    mena = tuple(t)
with open('priezviska.txt', "r", encoding="utf-8") as t:
    priezviska = tuple(t)

print("Študenti:\n================================")
studenti = list()
for i in range(pocet_studentov):
    meno = random.choice(mena)
    meno = meno[:-1]
    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]
    rok = random.randint(2005, 2008)
    if rok == 2005:
        trieda = "IV."
    elif rok == 2006:
        trieda = "III."
    elif rok == 2007:
        trieda = "II."
    else:
        trieda = "I."
    trieda = trieda + random.choice(("A", "B", "C"))
    studenti.append(Student(meno, priezvisko, rok, trieda))
for i in range(pocet_studentov):
    print(i, studenti[i].meno, studenti[i].priezvisko, studenti[i].vek, studenti[i].trieda)
print("================================\n")

print("Učitelia:\n================================")
ucitelia = list()
for i in range(pocet_ucitelov):
    meno = random.choice(mena)
    meno = meno[:-1]
    priezvisko = random.choice(priezviska)
    priezvisko = priezvisko[:-1]
    rok = random.randint(1955, 1998)
    trieda = random.choice(("I.", "II.", "III.", "IV.")) + random.choice(("A", "B", "C"))
    predmety = random.choice(("ANJ", "FYZ", "MAT", "TSV", "INF"))
    titul = random.choice(("Ing.", "Mgr."))
    if random.choice((1, 2)) == 1:
        ucitelia.append(Ucitel(meno, priezvisko, rok, predmety, trieda, titul))
    else:
        ucitelia.append(Ucitel(meno, priezvisko, rok, predmety, "", titul))
for i in range(pocet_ucitelov):
    print(i, ucitelia[i].titul, ucitelia[i].meno, ucitelia[i].priezvisko, ucitelia[i].vek, ucitelia[i].trieda)
print("================================\n")

idstudent = int(input("Zadaj ID študenta: "))
studenti[idstudent].pozdrav()
studenti[idstudent].vypis_triedny()

print("================================\n")
iducitel = int(input("Zadaj ID ucitela: "))
ucitelia[iducitel].pozdrav()
ucitelia[iducitel].vypis_ziakov()
