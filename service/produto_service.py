from entity.produto import Produto
from repository.produto_repository import ProdutoRepository

#Camada que armazena as regras de negócio 
class ProdutoService:
    def __init__(self):
        self.__repository = ProdutoRepository()

    
    def cadastrar(self, codigo, nome, valor):
        if codigo <= 0:
            raise ValueError("O código deve ser maior que 0")
        if nome == "":
            raise ValueError("O nome não pode ser vazio")
        if len(nome) > 30:
            raise ValueError("O nome não deve conter mais que 30 caracteres")
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero")
        produto = Produto(codigo,nome,valor)
        self.__repository.cadastrar(produto)

    def listar(self):
        return self.__repository.listar()