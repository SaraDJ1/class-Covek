class Covek:
    def __init__(self,godine):
        self.godine = godine
    def ProveriValidnost(self):
        if self.godine<0 or self.godine>100:
            print("Unesite druge godine")
            return False
        else:
            return True
    def ProveriGodine(self):
        if self.godine<18:
            print("Maloletan")
        if self.godine>18:
            print("Punoletan")

C1 = Covek(5)

if(C1.ProveriValidnost()):
    C1.ProveriGodine()



