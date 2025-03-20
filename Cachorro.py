class Cachorro:
    def __init__(self, nome, raca, comida, energia):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = False
        self.energia = 80

    def __str__(self):
        return f"Nome:  {self.nome}, Raça: {self.raca}, Comida: {self.comida}, Acordado: {self.acordado}, Feliz: {self.feliz}"
 

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} acordou!")
    
    def dormir(self):
        self.acordado = False
        print(f"{self.nome} acabou dormindo!")
    
    def passear(self):
        if self.feliz is True:
           print(f"{self.nome} foi passear e ficou feliz!")
        else:
            print(f"{self.nome} não está feliz!")
    
    def ignorar(self):
        if self.acordado is True:
           self.feliz = False
           print(f"Você ignorou {self.nome} e ficou triste")

    def brincar(self):
        if self.acordado:
            self.energia -= 20
            self.feliz = True
            print(f"{self.nome} está brincanco e está feliz.")
        else:
            print(f"{self.nome} não pode brincar, está dormindo...")

cachorro1 = Cachorro("Kiara", "SRD", 20)
cachorro1.passear()
