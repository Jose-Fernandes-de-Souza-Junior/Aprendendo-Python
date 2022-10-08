from tkinter import N


class Carro:
    def __init__ (self):
        self._nrodas = 4

    def set_nrodas (self,n):
        self._nrodas = n

gol = Carro()
print(gol._nrodas)

gol.set_nrodas(10)
print (gol._nrodas)

