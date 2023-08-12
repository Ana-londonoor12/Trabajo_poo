class Rectangulo:
    def __init__(self):
        self.esquina_sup_izq = (2, 4)
        self.esquina_inf_der = (1, 8)

    def calcular_perimetro(self):
        base = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        altura = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        altura = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina_inf_der[0] - self.esquina_sup_izq[0])
        altura = abs(self.esquina_inf_der[1] - self.esquina_sup_izq[1])
        return base == altura