from src.usecases.GeradorNF import GeradorNF

def test_gera_nota_fiscal():
  nome_cliente = "Carlos"
  endereco_cliente = "Rua A"
  tipo_servico = "CONSULTORIA"
  valor_fatura = 1000
  fatura = {
    "cliente": nome_cliente,
    "endereco": endereco_cliente,
    "tipo": tipo_servico,
    "valor": valor_fatura 
  }

  gerador_nf = GeradorNF()

  nf = gerador_nf.execute(fatura)
  assert nf["cliente"] == nome_cliente

def test_gera_nota_fiscal_25_imposto():
  nome_cliente = "Carlos"
  endereco_cliente = "Rua A"
  tipo_servico = "CONSULTORIA"
  valor_fatura = 1000
  fatura = {
    "cliente": nome_cliente,
    "endereco": endereco_cliente,
    "tipo": tipo_servico,
    "valor": valor_fatura 
  }

  gerador_nf = GeradorNF()

  nf = gerador_nf.execute(fatura)
  assert nf["valor"] == valor_fatura
  assert nf["imposto"] == valor_fatura * 0.25