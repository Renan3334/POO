class Cachorro:
    def __init__(self, nome, raca, comida):
        self.nome=nome
        self.comida=comida
        self.raca=raca
        self.acordado=True
        self.feliz=False
        self.energia = 80

    def __str__(self):
        return f"nome: {self.nome}, raça: {self.raca}, comida: {self.comida}, acordado: {self.acordado}, feliz: {self.feliz}"

    def comer(self):
        if self.comida>0:
            self.comida -=1
            self.feliz=True
            print(f"{self.nome} comeu e agora está feliz!")
        else: print(f"{self.nome} está sem comida!")

    def dormir (self):
            self.acordado = False
            print(f"{self.nome} dormindo.")

    def acordar (self):
            self.acordado = True
            print(f"{self.nome} está acordado!")    

    def brincar (self):
        if self.acordado:
            self.energia -= 20
            self.feliz = True
            print(f"{self.nome} está brincando e está feliz!")
        else:
            print(f"{self.nome} não pode brincar, está dormindo...")

    def ignorar (self):
            self.feliz = False
            print(f"{self.nome} está triste porque foi ignorado.")

    def latir (self):
        if self.acordado is True:
            print(f"{self.nome} está latindo: au au au!")
        else: print(f"{self.nome} está dormindo e não pode latir.")

Cachorro1 = Cachorro("Kira", "Chow-Chow", 20)
Cachorro1.comer()
Cachorro1.dormir()
Cachorro1.acordar()
Cachorro1.brincar()
Cachorro1.latir()
