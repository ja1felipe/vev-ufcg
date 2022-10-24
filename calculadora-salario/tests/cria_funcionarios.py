def test_cria_funcionario():
    nome = "masenko"
    email = "masenko@gmail.com"
    salario_base = 2000
    cargo = "desenvolvedor"

    funcionario = Funcionario(nome, email, salario_base, cargo)

    assert nome == funcionario.nome 
    assert email == funcionario.email 
    assert salario_base == funcionario.salario_base 
    assert cargo == funcionario.cargo 
    

def test_cria_funcionario_sem_nome():
    nome = "masenko"
    email = "masenko@gmail.com"
    salario_base = 2000
    cargo = "desenvolvedor"

    funcionario = Funcionario(nome, email, salario_base, cargo)

    assert nome == funcionario.nome 

def test_cria_funcionario_email_errado():
    nome = "masenko"
    email = "masenko@gmail.com"
    salario_base = 2000
    cargo = "desenvolvedor"

    funcionario = Funcionario(nome, email, salario_base, cargo)

    cargo_funcionario =  EnumCargos[cargo.upper()].value

    assert nome == funcionario.nome 


def test_cria_funcionario_cargo_inexistente():
    nome = "masenko"
    email = "masenko@gmail.com"
    salario_base = 2000
    cargo = "desenvolvedor"

    funcionario = Funcionario(nome, email, salario_base, cargo)

    cargo_funcionario =  EnumCargos[cargo.upper()].value

    assert nome == funcionario.nome 
