class Animal:
    def __init__(self):
        self.no_eyes = 2
    def breathe(self):
        print("Animals do Inhale and Exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("Fish can only breathe inside water.")
    def swim(self):
        print("Fish can swim")



animal = Animal()
nemo = Fish()
print(nemo.no_eyes)
nemo.breathe()