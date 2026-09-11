from entity.produto import Produto

#Camada Responsável pela gravação dos dados
class ProdutoRepository:
    def __init__(self):
        self.__produtos = []

    def cadastrar(self, produto):
        self.__produtos.append(produto)

    def listar(self):
        return self.__produtos