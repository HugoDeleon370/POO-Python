class Pessoa:
    def __init__(self, altura, cpf):
        self.altura = altura
        self.cpf = cpf

    def apresentar(self):
        print(f"Olá! Minha altura - {self.altura}")
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f"Meu documento - {self.cpf}")

jorge = Pessoa(1.70, 123456798)

jorge.apresentar()