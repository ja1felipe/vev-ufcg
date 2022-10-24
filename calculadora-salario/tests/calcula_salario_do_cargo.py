




def test_calcula_salario_desenvolvedor_equal_or_upper():

    salario_limite = 3000
    funcionario = Funcionario(nome, email, salario_base, cargo)

    cargo_funcionario =  EnumCargos[cargo.upper()].value

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == round(salario_limite * 0.8,1) 



def test_calcula_salario_desenvolvedor_lower():
    salario_limite = 2999
    funcionario = Funcionario(nome, email, salario_base, cargo)
    
    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == round(salario_limite * 0.9,1) 


def test_calcula_salario_dba_upper():
    salario_limite = 2000
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == round(salario_limite * 0.75,1) 

def test_calcula_salario_dba_lower():
    salario_limite = 1999
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == round(salario_limite * 0.85,1) 


def test_calcula_salario_testador_upper():
    salario_limite = 2500
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == round(salario_limite * 0.75,1) 


def test_calcula_salario_testador_lower():
    salario_limite = 1900
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == round(salario_limite * 0.85,1) 


def test_calcula_salario_gerente_upper():
    salario_limite = 5000
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == round(salario_limite * 0.7,1) 


def test_calcula_salario_gerente_lower():
    salario_limite = 3000
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == round(salario_limite * 0.8,1) 


