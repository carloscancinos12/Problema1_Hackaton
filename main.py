class Rectangulo:
    def __init__(self, x0: int, y0: int, x1: int, y1: int):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        print(self.calcular_area())

    def calcular_area(self):
        altura = self.y1 - self.y0
        ancho = self.x1 - self.x0
        return altura*ancho


def solicitar_rectangulo() -> Rectangulo:
    coordenadax0: int = int(input("Ingrese la coordenada en X de la esquina inferior izquierdo:"))
    coordenaday0: int = int(input("Ingrese la coordenada en Y de la esquina inferior izquierdo:"))
    coordenadax1: int = int(input("Ingrese la coordenada en X de la esquina superior derecha:"))
    coordenaday1: int = int(input("Ingrese la coordenada en Y de la esquina superior derecha:"))
    if coordenadax0 < coordenadax1 or coordenaday0 < coordenaday1:
        return Rectangulo(coordenadax0, coordenaday0, coordenadax1, coordenaday1)
    else:
        print("Ese rectangulo no es posible")
        return Rectangulo(0, 0, 0, 0)


def colisionador(rect1: Rectangulo, rect2: Rectangulo):
    altura: int = 0
    ancho: int = 0
    if rect1.y0 < rect2.y1 <= rect1.y1 and rect1.x0 < rect2.x1 <= rect1.x1:
        altura = rect2.y1 - rect1.y0
        ancho = rect2.x1 - rect1.x0
        if rect1.y0 < rect2.y0:
            altura -= rect2.y0 - rect1.y0
        if rect1.x0 < rect2.x0:
            ancho -= rect2.x0 - rect1.x0
    elif rect1.y1 > rect2.y0 >= rect1.y0 and rect1.x1 > rect2.x0 >= rect1.x0:
        altura = rect1.y1 - rect2.y0
        ancho = rect1.x1 - rect2.x0
        if rect2.y1 < rect1.y1:
            altura -= rect1.y1 - rect2.y1
        if rect2.x1 < rect1.x1:
            ancho -= rect1.x1 - rect2.x1
    return altura * ancho


rectangulos: list[Rectangulo] = []
print("Es necesario crear el primer rectangulo...")
rectangulos.append(solicitar_rectangulo())
repetir = True
rectError = Rectangulo(0, 0, 0, 0)
while repetir:
    print("1. Agregar otro rectangulo:")
    print("2. Calcular area disyuntiva exclusiva:")
    print("3. Salir:")
    try:
        opcion1 = int(input("Ingrese el numero de opcion que desea realizar:"))
    except:
        print('Esa no era una opcion')
        opcion1 = 0
    if opcion1 == 1:
        rect = rectError
        try:
            rect = solicitar_rectangulo()
        except:
            print('Algo a salido mal con el nuevo rectangulo')
        if rect != rectError:
            rectangulos.append(rect)
    elif opcion1 == 2:
        area = 0
        for rectangulo in rectangulos:
            area += rectangulo.calcular_area()
        for rectangulo in rectangulos:
            for rectangulo1 in rectangulos:
                if rectangulo1 != rectangulo:
                    area -= colisionador(rectangulo, rectangulo1)/2
        print(f"El area es: {area}")
    elif opcion1 == 3:
        repetir = False
