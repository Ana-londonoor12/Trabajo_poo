from modelo4.circulo import Circulo

mi_circulo = Circulo((0, 3), 6)
print("Área del círculo:", mi_circulo.calcular_area())
print("Perímetro del círculo:", mi_circulo.calcular_perimetro())

punto = (3, 4)
if mi_circulo.punto_pertenece(punto):
    print(f"El punto {punto} pertenece al círculo.")
else:
    print(f"El punto {punto} no pertenece al círculo.")
