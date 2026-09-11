class Produto:
    def __init__(self, codigo, nome, valor):
        self.__codigo = codigo
        self.__nome = nome
        self.__valor = valor

#trabalhando encapsulamento com propriedades
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property 
    def nome(self):
        return self.__nome
    
    @codigo.setter
    def nome(self, nome):
        self.__nome = nome

    @property 
    def valor(self):
        return self.__valor
    
    @codigo.setter
    def codigo(self, valor):
        self.__valor = valor

    
    def __str__(self):
        return f"{self.__codigo} -{self.__nome} - {self.__valor}"