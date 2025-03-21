class Carro:
    def __init__(self, marca, modelo, cor, combustivel, velocidade, ligado):
       self.marca = marca
       self.modelo = modelo
       self.cor = cor
       self.ligado = True
       self.desligado = True
       self.combustivel = 100
       self.velocidade = 0

    def __str__(self):
        return f"ligado: {self.ligado}, desligado: {self.desligado}, marca: {self.marca}, modelo: {self.modelo}, cor: {self.cor}, combustivel: {self.combustivel}"
    
    def ligar(self):
        if self.combustivel > 0:
            self.ligado is True
            return print("O carro está ligado!")
        else:
            return print("O carro não tem combustivel suficiente para ligar...")

    def desligado(self):
        if self.velocidade == 0:
            self.desligado is True
            return print("O carro está desligado!")
        else:
            return print("O carro não pode estar desligado enquanto está em movimento")

    def acelerar(self):
        if self.ligado and self.combustivel > 0:
            self.velocidade += 20
            self.combustivel -= 10
            return print("O carro está acelerando!!!")
        else:
            return print("O carro está parado...")

    def frear(self):
        if self.velocidade >= 20:
            self.velocidade -= 20
            return print("O carro está freando...!")
        else:
            self.velocidade = 0
            return print("O carro está parado...")

    def abastecer(self, quantidade):
        if self.combustivel + quantidade <= 100:
            self.combustivel += quantidade
        else:
            self.combustivel = 100
        return print(f"combustível abastecido. nível atual: {self.combustivel}")

    def buzinar(self):
        return print("BI BI BI BI!")

    def status(self):
        estado = "modelo: {}, ano: {}, cor: {}, combustível: {}, velocidade: {} km/h, ligado: {}.".format(
            self.modelo, self.ano, self.cor, self.combustivel, self.velocidade, "Sim" if self.ligado else "Não"
        )

carro1 = Carro("Fiat", "Palio", "Preto", 100, 0, True )
carro1.ligar()