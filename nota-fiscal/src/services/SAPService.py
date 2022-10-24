from src.entities.NotaFiscal import NotaFiscal

class SAP:
  def envia(self, nf: NotaFiscal) -> bool:
    print("enviando pro sap", nf.cliente)
    return True