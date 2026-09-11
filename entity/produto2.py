from dataclasses import dataclass


#função já vem com o construtor implementado
@dataclass
class Produto:
    codigo: int
    nome: str
    valor: float

