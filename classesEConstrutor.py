class Carro:
    def __init__(self, cor, nome, modelo):
        self.cor = cor
        self.nome = nome
        self.modelo = modelo
        
    def mostrarNome(self):
        print(self.nome)

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freiando...")


meu_carro = Carro("vermelho", "Fusca", "Volkswagen")


meu_carro.mostrarNome()



class Casa:
    def __init__(self, cor, material, bairro, numero, rua):
        self.cor = cor
        self.material = material
        self.bairro = bairro
        self.numero = numero
        self.rua = rua
    
    def mostrarMaterial(self):      
        self.material = "oi"
        print(self.material)


minhaCasa = Casa("vermelha", "tijolo", "jardins", "777", "rua da manga")
minhaCasa.mostrarMaterial()




class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)


        