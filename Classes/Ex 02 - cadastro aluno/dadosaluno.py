class dadosaluno:
    def __init__(self,nome,matricula,curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso


    def mostrar(self):
        print(f"Nome: {self.nome} \n Matricula: {self.matricula} \n Curso: {self.curso}")

    def alterar(self,novonome,novamatricula,novocurso):
        self.nome = novonome
        self.matricula = novamatricula
        self.curso = novocurso