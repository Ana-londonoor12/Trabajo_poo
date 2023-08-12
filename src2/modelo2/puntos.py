import math

class Puntos:
    def __init__(self):
        self.puntox = (5, 6)
        self.puntoy = (3, 7)
    
    def mostrar(self):
        print(f"({self.puntox[0]}, {self.puntox[1]}), ({self.puntoy[0]}, {self.puntoy[1]})")
    
    def mover(self, nuevo_X, nuevo_Y):
        self.puntox = (nuevo_X, self.puntox[1])
        self.puntoy = (nuevo_Y, self.puntoy[1])
  
    def obtener_coordenadas(self):
        return self.puntox, self.puntoy
    
    def calcular_distancia(self, punto_diferente):
        Distancia_x = punto_diferente.puntox[0] - self.puntox[0]
        Distancia_y = punto_diferente.puntoy[1] - self.puntoy[1]
        Distancia = math.sqrt(Distancia_x ** 2 + Distancia_y ** 2)
        return Distancia
    
   
  


    





   
        



   

