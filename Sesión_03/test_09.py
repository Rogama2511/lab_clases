"""Listas en Python"""

"""Listas -> del: Eliminará un valor indicando el índice del valor de la lista"""

paises = []

paises.append("Perú")
paises.append("Brasil")
paises.append("Argentina")
paises.append("Canadá")
paises.append("México")
paises.append("Guatemala")

print(paises)

del paises[2]

print("Mi lista actualizada tienes estos valores {}".format(paises))

del paises[4]

print("Mi lista actualizada tienes estos valores {}".format(paises))