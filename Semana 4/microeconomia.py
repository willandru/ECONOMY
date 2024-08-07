import numpy as np


def punto_de_equilibrio(a, b, c, d):

    #   a -> intercepto curva demanda
    #   b -> pendiente curva demanda
    #   c -> intercepto curva oferta
    #   d -> pendiente curva oferta
    #  La funcion de la Demanda es: Qd= a-bP
    #  La funcion de la Oferta es: Qs= c+dP
    
    #print("Sus funciones ingresadas fueron: ")
    #print(f"Qd={b}*p + {a}")
    #print(f"Qs={d}*P + {c}")

    # Definir la matriz de coeficientes A y el vector de términos constantes B
    A = np.array([[1, -b],
                  [1, -d]])
    B = np.array([a, c])
    
    # Resolver el sistema de ecuaciones
    try:
        X = np.linalg.solve(A, B)
        # Extraer los valores de x e y
        y, x = X
        print(f"P.E: (P={x}, Q={y})")
    except np.linalg.LinAlgError:
        print("Las rectas son paralelas y no tienen un punto de equilibrio.")

def elaticidad_precio_demanda(b,p,q):

    # b->pendiente de la demanda, NO incluir el signo.
    # p -> precio de equilibrio
    # q -> cantidad de equilibrio

    e= -p*b/q
    print(f"Elasticidad precio-demanda(b={b},p={p},q={q}): e=", e)
    return e

def elaticidad_precio_oferta(d,p,q):

    # d->pendiente de la oferta
    # p -> precio de equilibrio
    # q -> cantidad de equilibrio

    n= p*d/q
    print(f"Elasticidad precio-oferta(d={d},p={p},q={q}): n=", n)
    return n

def pendientes_oferta_demanda(e,n,p,q):

    b=(e*q)/(-p)
    d=(n*q)/p

    print(f"Pendiente Demanda(e={e},p={p},q={q}): b=", b)
    print(f"Pendiente Oferta(n={n},p={p},q={q}): d=", d)

    return b, d

def interceptos_oferta_demanda(b,d,p,q):

    a=q+b*p
    c=q-d*p

    print(f"Intercepto Demanda(b={b},p={p},q={q}): a=", a)
    print(f"Intercepto Oferta(d={d},p={p},q={q}): c=", c)
    return a, c

def calcular_actividad2(b,d,p,q):
    #Elasticidades
    e = elaticidad_precio_demanda(b,p,q)
    n = elaticidad_precio_oferta(d,p,q)
    #Pendientes
    b , d = pendientes_oferta_demanda(e,n,p,q)
    #Interceptos
    a, c = interceptos_oferta_demanda(b,d,p,q)

# PUNTOS DE EQUILIBRIO
punto_de_equilibrio(1000, -2, 500, 8)
punto_de_equilibrio(400, -1, 200, 3)
punto_de_equilibrio(150, -3, 30, 3)
punto_de_equilibrio(198, -5, 101.6, 3)
punto_de_equilibrio(944, -1, 400, 2)


# ELASTICIDAD PRECIO DEMANDA 

e1 = elaticidad_precio_demanda(2, 50, 900)
e2 = elaticidad_precio_demanda(1,50,350)

# ELASTICIDAD PRECIO OFERTA

n1 = elaticidad_precio_oferta(8,50,900)
n2 = elaticidad_precio_oferta(3,50,350)

# PENDIENTES CURVAS OFERTA Y DEMANDA

b1, d1 = pendientes_oferta_demanda(-0.111, 0.444, 50, 900)
b2, d2 = pendientes_oferta_demanda(-0.143, 0.429, 50, 350)

# INTERCEPTO DE LA OFERTA Y DEMANDA

a1, c1 = interceptos_oferta_demanda(2,8,50,900)
a2, c2 = interceptos_oferta_demanda(1,3,50,350)

print("##############################")
print("#########PRIMERO###########")
calcular_actividad2(2, 8, 50, 900)
print("#########SEGUNDO###########")
calcular_actividad2(1,3,50,350)
print("#########TERCERO###########")
calcular_actividad2(3,3,20,90)
print("#########CUARTO###########")
calcular_actividad2(5,3,12.05,137.75)
print("#########QUINTO###########")
calcular_actividad2(1,2,181.3,762.66)