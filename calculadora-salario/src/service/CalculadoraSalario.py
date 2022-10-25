from src.entities.Funcionario import Funcionario
from src.enums.EnumCargo import EnumCargos

class CalculadoraSalario:
  def retorna_salario_por_cargo(self, funcionario: Funcionario) -> float:
    salario_calculado = 0
    
    if(funcionario.cargo.upper() == EnumCargos.DESENVOLVEDOR.value):
        if(funcionario.salario_base >= 3000):
            salario_calculado = funcionario.salario_base * 0.8
        else:
            salario_calculado = funcionario.salario_base * 0.9

    if(funcionario.cargo.upper() == EnumCargos.DBA.value or funcionario.cargo.upper() == EnumCargos.TESTADOR.value):
        if(funcionario.salario_base >= 2000):
            salario_calculado = funcionario.salario_base * 0.75
        else:
            salario_calculado = funcionario.salario_base * 0.85
    
    if(funcionario.cargo.upper() == EnumCargos.GERENTE.value):
        if(funcionario.salario_base >= 5000):
            salario_calculado = funcionario.salario_base * 0.7
        else:
            salario_calculado = funcionario.salario_base * 0.8
    
    
    return salario_calculado 