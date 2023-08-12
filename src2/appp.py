from modelo2.puntos import Puntos

PuntosXY = Puntos()
print("Mi coordenada del punto X:", PuntosXY.puntox)
print("Mi coordenada del punto Y:", PuntosXY.puntoy)

punto1 = Puntos()
print("Coordenadas iniciales:", punto1.obtener_coordenadas())

punto1.mover(0, 2)
print("Coordenadas movidas son:", punto1.obtener_coordenadas())

punto1 = Puntos((5, 6), (3, 7))
punto2 = Puntos((0, 2), (1, 9))
Distancia = punto1.calcular_distancia(punto2.obtener_coordenadas())
print("La distancia entre puntos es:", Distancia)








