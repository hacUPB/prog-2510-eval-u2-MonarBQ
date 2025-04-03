'''
Actividad 1:
INICIO
    Leer num1
    Leer num2
    resta = valor1 - valor2
    Mostrar resta
FIN
'''

'''
Pregunta orientadora:
La diferencia entre float(input) y int(input) es que el primero convierte la entrada a decimales y el segundo
a enteros.
'''

'''
Actividad 2:
INICIO
    Ler n1, n2, n3, ... , nt
    Promedio = (n1+n2+n3+...+nt)/t
    Mostrar Promedio
FIN
'''
# Reto Final

# Pseudocodigo 1
'''
X1 = float(input("Ingrese X1: "))
X2 = float(input("Ingrese X2: "))
Y1 = float(input("Ingrese Y1: "))
Y2 = float(input("Ingrese Y2: "))
C1 = float(input("Ingrese C1: "))
C2 = float(input("Ingrese C2: "))
D = ((C1 ** 2) + (C2 ** 2)) ** (1/2)

print(f"C={D}")
'''
# Pseudocodigo 2
'''
M = float(input("Ingrese M: "))
P = 0.0254
T = M / P

print("T =", T)
'''
# Pseudocodigo 3
'''
A = float(input("Ingrese A: "))
B = float(input("Ingrese B: "))
C = (A**2 + B**2) ** 0.5

print("C =", C)
'''
# Pseudocodigo 4
'''
DN = int(input("Ingrese el día de nacimiento: "))
MN = int(input("Ingrese el mes de nacimiento: "))
AN = int(input("Ingrese el año de nacimiento: "))
DA = int(input("Ingrese el día actual: "))
MA = int(input("Ingrese el mes actual: "))
AA = int(input("Ingrese el año actual: "))

EA = AA - AN

if MA < MN:  
    EA = EA - 1
elif MA == MN: 
    if DA < DN:
        EA = EA - 1
    elif DA == DN:
        print("FELIZ CUMPLEAÑOS")
    else:
        print("Edad actual:", EA)
else:
    print("Edad actual:", EA)
'''
#Pseudocodigo 5
'''
VH = float(input("Ingrese el valor por hora: "))
HT = float(input("Ingrese las horas trabajadas: "))
if HT > 50:
    print("ERROR (No se puede trabajar más de 50 horas)")
else:
    if HT > 45:
        SS = ((HT - 45) * (VH * 3)) + ((VH * 2) * 5) + (40 * VH)
    elif HT > 40:
        SS = ((HT - 40) * (VH * 2)) + (40 * VH)
    else:
        SS = HT * VH
    print("Salario semanal: $", SS)
'''

