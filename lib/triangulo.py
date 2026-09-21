def get_identificador()->str:
    return 'triángulo'

def get_area(base:int, altura:int)->float:
    area = (base*altura)/2
    return area


def get_perimetro(lado_a:int, lado_b:int, lado_c:int)->int:
    perimetro = lado_a + lado_b + lado_c
    return perimetro

