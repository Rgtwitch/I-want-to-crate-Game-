class info:

    health = 10
    expiriance = 0
    maxexpiriance = 2
    strenght = 10
    mana = 100
    level = 1

    def getInfo(self):
        print(self.health)
        print(self.strenght)
        print(self.mana)
        print("+" * self.expiriance, "-" * (self.maxexpiriance - self.expiriance), self.expiriance)
        print(self.level)

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
            print("Показатели персонажа возросли!")
            self.health = self.mana + self.mana

