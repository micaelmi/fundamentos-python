class Veiculo:
  def __init__(self, cor, rodas, marca, modelo, tanque):  
    self.cor = cor
    self.rodas = rodas
    self.marca = marca
    self.modelo = modelo
    self.tanque = tanque
    
  def abastecer(self, litros):
    self.tanque += litros