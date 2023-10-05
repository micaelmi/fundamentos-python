from veiculo import Veiculo
from carro import Carro

veiculo1 = Carro('dourado', 'bmw', 'pegasus4', 35)

print(type(veiculo1))
print(veiculo1)

print("modelo:",veiculo1.modelo) 
print("cor:",veiculo1.cor)
print("tanque:", veiculo1.tanque)

print("")
veiculo2 = Veiculo('rosa', 8, 'mercedes', 'r900', 20)

print("modelo:",veiculo2.modelo)
print("cor:",veiculo2.cor)
print("tanque:", veiculo2.tanque)

veiculo2.abastecer(35)
print("\nabastecendo...")
print("tanque:", veiculo2.tanque)

print("\nAbastecendo", veiculo1.modelo)
veiculo1.abastecer(100)
print("tanque:", veiculo1.tanque)