class info(object):

    def __init__(self):
        self.health = 10
        self.expiriance = 0
        self.maxexpiriance = 2
        self.strenght = 10
        self.mana = 100
        self.level = 1
        self.localization = 0


    def ChoseLocal(self):
        print("Choose localization:")
        print("Eng")
        print("Rus")
        self.localization = input()

    def getInfo(self):
        if self.localization == "Rus":
            print("Здоровье -", self.health)
            print("Сила -", self.strenght)
            print("Мана -", self.mana)
            print("Опыт -", "+" * self.expiriance, "-" * (self.maxexpiriance - self.expiriance), self.expiriance)
            print("Уровень -", self.level)
        elif self.localization == "Eng":
            print("Health -", self.health)
            print("Strenght -", self.strenght)
            print("Mana -", self.mana)
            print("Experience -", "+" * self.expiriance, "-" * (self.maxexpiriance - self.expiriance), self.expiriance)
            print("Level -", self.level)
    def getHelth(self):
        return self.health

    def getStrenght(self):
        return self.strenght

    def getMana(self):
        return self.mana

    def getExp(self):
        return self.expiriance

    def getLvl(self):
        return self.level

    def addHelth(self, count):
        self.health = self.health + count

    def addStrenght(self, count):
        self.strenght = self.strenght + count

    def addMana(self, count):
        self.mana = self.strenght + count

    def addExpiriance(self, count):
        self.expiriance = self.expiriance + count
        if self.expiriance >= self.maxexpiriance:
            self.maxexpiriance = self.maxexpiriance * 2
            self.level += 1
            BeAChose = False
            while not BeAChose:
                if self.localization == "Eng":
                    print("Skill point available!")
                    print("1 - Mana")
                    print("2 - Strenght")
                    print("3 - Health")
                elif self.localization == "Rus":
                    print("Доступно очко навыков!")
                    print("1 - Мана")
                    print("2 - Сила")
                    print("3 - Жизни")
                chose = int(input())
                if chose == 1:
                    self.mana = self.mana + (self.mana // 2)
                    BeAChose = True
                    if self.localization == "Eng":
                        print("Mana =", self.mana)
                    if self.localization == "Rus":
                        print("Мана", self.mana)
                elif chose == 2:
                    self.strenght = self.strenght + (self.strenght // 2)
                    BeAChose = True
                    if self.localization == "Eng":
                        print("strenght =", self.strenght)
                    if self.localization == "Rus":
                        print("Сила =", self.strenght)
                elif chose == 3:
                    self.health = self.strenght + (self.strenght // 2)
                    BeAChose = True
                    if self.localization == "Eng":
                        print("Health =", self.health)
                    if self.localization == "Rus":
                        print("Жизни", self.health)
