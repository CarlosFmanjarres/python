
Nombre = input("Ingrese el nombre de empleado")
Hijos = int(input("ingrese el numero de hijos que tiene el empleado"))
if (Hijos >= 3):
    bonificación_hijos =int(Hijos * 10)
    print(f"la bonificación por hijos es de: {bonificación_hijos} horas" )
else:
    bonificación_hijos = int(Hijos * 5)
    print(f"la bonificación por hijos es de: {bonificación_hijos} horas")

valor_hora = 4000
nro_horas_semana = int(input("ingrese el numero de horas que trabaja por semana"))
valor_horas_trabajadas = int(nro_horas_semana*valor_hora)
print(valor_horas_trabajadas)
horas_extras=int(input("ingrese las horas extras trabajadas: "))
valor_horas_extras=int(5400*horas_extras)
print(f"el valor de las horas extras es de : {valor_horas_extras}")
devengado=int(valor_horas_extras+valor_horas_trabajadas)
print(f"el devengado tiene un valor de: {devengado}")
bonificacion=int(valor_horas_extras+(5400*bonificación_hijos))
pago_neto=int(devengado+bonificacion)
print(f"el pago neto es de: {pago_neto}")

print("nombre:",Nombre, "\nnro de hijoos ",Hijos,"\nbonificación por hijos",bonificación_hijos,"\nvalor hora",valor_hora,"\nhoras trabajadas",nro_horas_semana,"\nvalor de las horas",valor_horas_trabajadas,"\nhoras extras",horas_extras,"\nvalor de las extras",valor_horas_extras,"\ndevengado",devengado,"\nneto a pagar",pago_neto,)





