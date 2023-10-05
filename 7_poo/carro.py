from veiculo import Veiculo

class Carro(Veiculo):
  def __init__(self, cor, marca, modelo, tanque):
    super().__init__(cor, 4, marca, modelo, tanque)  
    
  def abastecer(self, litros):
    if self.tanque + litros > 60:
      self.tanque = 60
      print("Tanque cheio")