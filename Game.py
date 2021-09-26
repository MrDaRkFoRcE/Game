import random
rand = random.randint(0, 100)
a = 1
b = 2
c = 3

try:
    def HadsAdad():
        while True:
            randuser = int(input("Enter : "))
            if rand == randuser:
                print("Shoma Barande Shodid !")
            elif rand > randuser:
                print("Rand > ", randuser)
            elif rand < randuser:
                print("Rand < ", randuser)
            else:
                print("Vorodi Na Motabar Ast !")
                continue
    def SangKaghazQeychi():
        while True:
            mashin = random.randint(a,c)
            user = int(input("1.Sang\n2.Kaqhaz\n3.Qeychi\nEnter : "))
            if (user != 1) and (user != 2) and (user != 3):
                print("Vorodi Na Motabar Ast ! ")
                continue
            elif (mashin == 1 and user == 2) or (mashin == 2 and user == 3) or (mashin == 3 and user == 1):
                print("Shoma Barande Shodid !")
            elif mashin == user:
                        print("Bazi Mosavi Shod !")
            elif (user == 1 and mashin == 2) or (user == 2 and mashin == 3) or (user == 3 and mashin == 1):
                print("Shoma Bakhtid !")
            else:
                print("Vorodi Na Motabar Ast ! ")
                continue
            if mashin == 1:
                print("Entekhab Mashin : 1.Sang ")
            elif mashin == 2:
                print("Entekhab Mashin : 2.Kaghaz ")
            elif mashin == 2:
                print("Entekhab Mashin : 3.Qeychi ")
            else:
                print("Vorodi Na Motabar Ast ! ")
                continue
except ValueError:
    print("Vorodi Na Motabar Ast ! ")

entergame = int(input("1.Hads Adad\n2.Sang Kaqhaz Qeychi\nBazi Khod Ra Entekhab Konid : "))
print("")
if (entergame != 1) and (entergame != 2):
    print("Vorodi Na Motabar Ast ! ")
elif entergame == 1:
    HadsAdad()

elif entergame == 2:
    SangKaghazQeychi()

else:
    print("Vorodi Na Motabar Ast ! ")
