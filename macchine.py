class Macchine:
    def __init__ (self, marca, modello, colore, anno, targa):
        self.marca=marca
        self.modello=modello
        self.colore=colore
        self.anno=anno
        self.targa=targa

    def __str__(self):
        return f'({self.marca},{self.modello},{self.colore},{self.anno},{self.targa})'
    

macchina=Macchine('Pagani','Huayra','White',2019,'PGN123HY')
print(macchina.__str__())