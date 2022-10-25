from src.entities.Funcionario import Funcionario
from src.service.CalculadoraSalario import CalculadoraSalario

def test_calcula_salario_desenvolvedor_equal_or_upper():

    nome = "cenobita"
    email = "cenobita@gmail.com"
    salario_base = 3000
    cargo = "desenvolvedor"

    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == salario_base * 0.8



def test_calcula_salario_desenvolvedor_lower():
    
    nome = "cenobita"
    email = "cenobita@gmail.com"
    cargo = "desenvolvedor"
    salario_base = 2999
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == salario_base * 0.9 


def test_calcula_salario_dba_upper():
    nome = "cenobita"
    email = "cenobita@gmail.com"
    cargo = "dba"
    salario_base = 2000

    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == salario_base * 0.75

def test_calcula_salario_dba_lower():
    nome = "cenobita"
    email = "cenobita@gmail.com"
    cargo = "dba"
    salario_base = 1999

    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == salario_base * 0.85


def test_calcula_salario_testador_upper():
    nome = "cenobita"
    email = "cenobita@gmail.com"
    cargo = "testador"
    salario_base = 2500
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == salario_base * 0.75


def test_calcula_salario_testador_lower():
    nome = "cenobita"
    email = "cenobita@gmail.com"
    cargo = "testador"
    salario_base = 1900
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == salario_base * 0.85


def test_calcula_salario_gerente_upper():
    nome = "cenobita"
    email = "cenobita@gmail.com"
    cargo = "gerente"
    salario_base = 5000
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == salario_base * 0.7


def test_calcula_salario_gerente_lower():
    nome = "cenobita"
    email = "cenobita@gmail.com"
    cargo = "gerente"
    salario_base = 3000
    funcionario = Funcionario(nome, email, salario_base, cargo)

    calcula_salario = CalculadoraSalario()

    salario_final = calcula_salario.retorna_salario_por_cargo(funcionario)    

    assert salario_final == salario_base * 0.8


