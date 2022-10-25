from src.enums.EnumCargo import EnumCargos

class Funcionario:
    def __init__(self, nome: str, email: str, salario_base: int, cargo: EnumCargos) -> None:
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo
    