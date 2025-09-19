from lib import cuadrado, rectantulo
print("Proyecto figuras")
print(cuadrado.get_identificador)
lado=4
print(f"El área de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)} y el perímetro es: {cuadrado.get_perimetro(lado)}")
#prueba
#prueba2

base=4
altura=2
print(f"El área de un rectángulo de base {base} y altura {altura} es: {rectantulo.get_area(base, altura)} y el perímetro es: {rectantulo.get_perimetro(base, altura)}")