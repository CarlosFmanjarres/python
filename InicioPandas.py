import pandas as pd

nombreEstudiantes= ["melisa","mateo","david","alejandra"]

print(nombreEstudiantes)

print("****** imprimir serie de pandas")
serieNombres =pd.Series(nombreEstudiantes)
print(serieNombres)

#imprimir un elemento de la serie
print(len(serieNombres))
print(serieNombres[len(serieNombres)-1])



