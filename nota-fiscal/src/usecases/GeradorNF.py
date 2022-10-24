from src.entities.Fatura import Fatura
from src.entities.NotaFiscal import NotaFiscal

class GeradorNF:
  def execute(self, fatura: Fatura) -> NotaFiscal:
    imposto = fatura.valor * 0.25
    return NotaFiscal(fatura.cliente, fatura.valor, imposto) 