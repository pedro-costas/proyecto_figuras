from lib import cuadrado, triangulo, rectangulo, circunferencia
from math import pi
print("Proyecto Figuras")

print(cuadrado.get_identificador())
lado=4
print(f"El área de un {cuadrado.get_identificador()} de lado {lado} es: {cuadrado.get_area(lado)} y el perimetro es {cuadrado.get_perimetro(lado)}")

base=4
altura=2
radio = 3

print(triangulo.get_identificador())
print(f"El área de un {triangulo.get_identificador()} de base {base} y altura {altura} es: {triangulo.get_area(base, altura)} y el perimetro es {triangulo.get_perimetro(base, base, base)}")

print(rectangulo.get_identificador())
print(f"El área de un {rectangulo.get_identificador()} de base {base} y altura {altura} es: {rectangulo.get_area(base, altura)} y el perímetro es {rectangulo.get_perimetro(base,altura)}")

print(circunferencia.get_identificador())
print(f"El área de una circunferencia de radio {radio} es: {circunferencia.get_area(radio)}")