class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()


while True:
    an.party()
    if an.x == 200:
        print("Too many animals. Shutting down.")
        break
        
