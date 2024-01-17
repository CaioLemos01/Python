m = 0.897 #kg
r = 0.12 #m
g = 9.8 #CTE
h = 0.67 #CTE
t1 = 11.03 #s
t2 = 7.6 #CTE / s
ict = 1/3 #CTE
ictTime = 0.24 

# Derivadas Parciais

d1 = (((((r**2)*g)/(2*h)))**2) * ((0.001**2)/3) # Derivada Parcial em relação a massa
d2 = ((((r*g*m)/h))**2) * (0.005**2) # Derivada Parcial em relação ao raio
d3 = (((((r**2)*g*m)/(h**2)))**2 * (((0.01)**2)/3)) # Derivada Parcial em relação a altura
d4 = ((((r**2)*g*m)/(2*h)*2*t1)**2 * (ictTime)**2) # Derivada Parcial em relação ao tempo
d5 = (((((r**2)*g*m)/(2*h))*((2*t2)))**2 * (0.23)**2) # Derivada Parcial em relação ao tempo

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)

incerteza = (d1 + d2 + d3 + d4 + d5)**0.5

print(f'Incerteza: {incerteza}')