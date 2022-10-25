from src.entities.Funcionario import Funcionario
from src.utils.validate import check_cargo,check_email

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
    nome = ""
    email = "masenko@gmail.com"
    salario_base = 2000
    cargo = "desenvolvedor"

    funcionario = Funcionario(nome, email, salario_base, cargo)

    assert len(funcionario.nome) == 0

def test_cria_funcionario_email_invalido():
    nome = "masenko"
    email = "masenko.com"
    salario_base = 2000
    cargo = "desenvolvedor"

    funcionario = Funcionario(nome, email, salario_base, cargo)

    email_flag = check_email(funcionario.email)
    
    assert not email_flag 


def test_cria_funcionario_cargo_inexistente():
    nome = "masenko"
    email = "masenko@gmail.com"
    salario_base = 2000
    cargo = "malabarista"

    funcionario = Funcionario(nome, email, salario_base, cargo)

    cargo_flag = check_cargo(funcionario.cargo)

    assert not cargo_flag 
