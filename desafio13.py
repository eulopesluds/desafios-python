dias = int(input())
anos = dias / 365
anos = int(anos)
dias_restantes = dias - (anos * 365)
meses = dias_restantes / 30
meses = int(meses)
dias_restantes = dias_restantes - (meses * 30)
print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias_restantes, "dia(s)")