mes1=float(input("Primer parcial: "))
mes2=float(input("Segundo parcial: "))
mes3=float(input("Tercer parcial: "))
#recuerda usar jerarquia de operaciones
promedio=(mes1+mes2+mes3)/3
#Condicionamos a que la calificacion sea aprobatoria
if promedio>=7:
    print("Felicidades, aprobaste.")
else:
    print("Pregunta por el examen extraordinario.")
print("Gracias por utilizar nuestros servicios.")