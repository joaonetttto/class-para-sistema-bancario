class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nome}| {self.categoria } '
    
    @classmethod
    def listar_restaurante(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
            
    def alternar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "verdadeiro" if self._ativo else "false"
    

restaurante_praca = Restaurante("praça", "gourmet")
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante("pizza express", "italiana")

Restaurante.listar_restaurante()
