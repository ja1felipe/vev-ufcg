from src.enums.TipoFatura import TipoFatura
from src.entities.Fatura import Fatura
from src.usecases.GeradorNF import GeradorNF

def test_deve_enviar_sap():
  sap = SAP()
  nome_cliente = "Carlos"
  endereco_cliente = "Rua A"
  tipo_servico = TipoFatura.CONSULTORIA
  valor_fatura = 1000
  fatura = Fatura(nome_cliente, endereco_cliente, tipo_servico, valor_fatura)

  gerador_nf = GeradorNF()

  nf = gerador_nf.execute(fatura)

  res = sap.envia(nf)

  assert res == True