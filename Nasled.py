class Beard():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name}  летает")

    def eat(self):
        print(f"{self.name}  кушает")

    def sing(self):
        print(f"{self.name}  поёт  -  {self.voice}")

    def info(self):
         print(f"{self.name} - имя")
         print(f"{self.voice} - голос")
         print(f"{self.color} - окрас")

class Pigeon(Beard):
    #pass
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name}  поёт  -  курлык")

    def walk(self):
        print(f"{self.name}  гуляет")

biord1 = Pigeon("Гоша", "курлык", "серый", "хдебные крошки")

biord1.sing()
biord1.info()

biord1.walk()
biord2 = Beard("Маша", "чирик", "коричневый")


