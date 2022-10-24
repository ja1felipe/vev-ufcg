from src.entities.Fatura import Fatura
from src.entities.NotaFiscal import NotaFiscal

class GeradorNF:
  def execute(self, fatura: Fatura):
    nf = fatura
    imposto = fatura.valor * 0.25
    return NotaFiscal(nf.cliente, nf.valor, imposto) 