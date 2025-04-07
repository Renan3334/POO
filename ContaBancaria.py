class Contabancaria:
    def __init__(self, titular, saldo, limite):
        self._titular = titular #público = "."
        self._saldo = saldo #privados = "._"
        self._limite = limite
    
    def set_limite(self, limite):
       if limite >=0:
          self._limite = limite
       else:
            print("O limite não foi estab   elecido!")
    
    def depositar(self, valor):
       if valor > 0:
          self._saldo += valor
          print("O depósito de R$ {:.2f} foi realizado".format (valor))
       else:
          print("O depósito não foi realizado!")

    def sacar(self,valor):
       if valor > 0:
          if valor <=  (self._saldo + self._limite):
             self._saldo -= valor
             print("O saque de {:.2f} foi realizado!".format(valor))
       else:
          print("O saque não foi realizado!")
          
    def get_saldo(self):
        return self._saldo

    def set_saldo(self, valor):
        if valor >=0:
         self._saldo = valor
        else:
           print("Valor negativo inválido!!!")
       
conta1 = Contabancaria("Weslley", 1000.00, 3000.00)
conta1.sacar(900)
print("O novo saldo é de :{}".format (conta1.get_saldo())
