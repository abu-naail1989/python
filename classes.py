class User:
    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print("Attcking with power of {}".format(self.power))


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print("attacking with arrows of {}".format(self.num_of_arrows))


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self,name, arrows)
        Wizard.__init__(self,name, power)


wizard1 = Wizard("Kofi", 50, "kofi@gmail.com")
archer1 = Archer("Yaw", 20)

print(wizard1.email)


