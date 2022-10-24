from copyreg import constructor


class GeradorNF:
  def execute(self, fatura):
    nf = fatura
    imposto = fatura["valor"] * 0.25
    nf["imposto"] = imposto
    return nf 