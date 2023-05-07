class Ventana:
    def __init__(self, titulo, x1=0, y1=0, x2=500, y2=500):
        self.titulo = titulo
        self.x1 = x1 if x1 >= 0 else 0
        self.y1 = y1 if y1 >= 0 else 0
        self.x2 = x2 if x2 <= 500 else 500
        self.y2 = y2 if y2 <= 500 else 500

    def mostrar(self):
        print(f'Ventana {self.titulo}: x1={self.x1} y1={self.y1} x2={self.x2} y2={self.y2}')

    def moverDerecha(self, unidades=1):
        self.x1 += unidades
        self.x2 += unidades
        if self.x2 > 500:
            self.x2 = 500
            self.x1 = 500 - (self.x2 - self.x1)

    def moverIzquierda(self, unidades=1):
        self.x1 -= unidades
        self.x2 -= unidades
        if self.x1 < 0:
            self.x1 = 0
            self.x2 = self.x1 + (self.x2 - self.x1)

    def subir(self, unidades=1):
        self.y1 -= unidades
        self.y2 -= unidades
        if self.y1 < 0:
            self.y1 = 0
            self.y2 = self.y1 + (self.y2 - self.y1)

    def bajar(self, unidades=1):
        self.y1 += unidades
        self.y2 += unidades
        if self.y2 > 500:
            self.y2 = 500
            self.y1 = 500 - (self.y2 - self.y1)

    def alto(self):
        return abs(self.y2 - self.y1)

    def ancho(self):
        return abs(self.x2 - self.x1)

    def getTitulo(self):
        return self.titulo
