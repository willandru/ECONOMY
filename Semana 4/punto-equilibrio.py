import numpy as np


def punto_de_equilibrio(a, b, c, d):

    #   a -> intercepto curva demanda
    #   b -> pendiente curva demanda
    #   c -> intercepto curva oferta
    #   d -> pendiente curva oferta
    #  La funcion de la Demanda es: Qd= a-bP
    #  La funcion de la Oferta es: Qs= c+dP
    print("Sus funciones ingresadas fueron: ")
    print(f"Qd={b}*p + {a}")
    print(f"Qs={d}*P + {c}")

    # Definir la matriz de coeficientes A y el vector de términos constantes B
    A = np.array([[1, -b],
                  [1, -d]])
    B = np.array([a, c])
    
    # Resolver el sistema de ecuaciones
    try:
        X = np.linalg.solve(A, B)
        # Extraer los valores de x e y
        y, x = X
        print(f"El Punto de Equilibrio es: (P={x}, Q={y})")
    except np.linalg.LinAlgError:
        print("Las rectas son paralelas y no tienen un punto de equilibrio.")

# Ejemplo de uso
punto_de_equilibrio(1000, -2, 500, 8)
punto_de_equilibrio(400, -1, 200, 3)
punto_de_equilibrio(150, -3, 30, 3)
punto_de_equilibrio(198, -5, 101.6, 3)
punto_de_equilibrio(944, -1, 400, 2)
