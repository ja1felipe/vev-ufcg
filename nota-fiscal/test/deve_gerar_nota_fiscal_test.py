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
