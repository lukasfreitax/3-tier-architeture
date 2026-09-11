from service.produto_service import ProdutoService

class ProdutoView:
    def __init__(self):
        self.__service = ProdutoService()

    def exibir_menu(self):
        opcao = ""
        while opcao != "9":
            print("Menu","1-Cadastrar","2-Listar","9-Sair")
            opcao = input("Informe uma opção: ")
            if opcao == "1":
                try:
                    codigo = int(input("Informe o código: "))
                    nome = input("Informe o nome: ")
                    valor = float(input("Informe o valor: "))
                    self.__service.cadastrar(codigo, nome, valor)
                    print("Produto cadastrado!!")
                except ValueError as e:
                    print(f"Erro: {e}")
            elif opcao == "2":
                for item in self.__service.listar():
                    print(item)
            elif opcao == "9":
                print("Finalizando... ")
            else:
                print("Opção inválida!")
                