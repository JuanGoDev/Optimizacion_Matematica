# Function

# def f(x): return 4 - x ** 2 - 0.2 * x ** 3
import math


def f(x): return 20 * x ** 6 - 13 * x ** 5 + 2 * \
    x ** 4 - 8 * x ** 3 + 13 * x ** 2 - 2 * x + 1


# Estimación inicial
# xl = -2
# xu = 1
xl = 2
xu = -2
#################################

# Crear puntos interiores iniciales. x1 y x2 y evaluar la función en cada punto
K = 0.5*(1+math.sqrt(5))
i = 1
I1 = xu - xl
I2 = I1/K
xak = xu - I2
xbk = xl + I2
fak = f(xak)
fbk = f(xbk)
Ik1 = I2
xLk = xl
xUk = xu

print(K, i, I1, I2, xak, xbk, fak, fbk, Ik1, xLk, xUk)
print(math.exp(-5))
print(type(math.exp(-5)))
print(Ik1 >= math.exp(-5) & xak <= xbk)

# Método de búsqueda de la Golden-Section

while Ik1 >= math.exp(-5) & xak <= xbk:
    Ik2 = Ik1/K

    if fak >= fbk:
        xLk1 = xak
        xUk1 = xUk
        xak1 = xbk
        xbk1 = xLk1 + Ik2
        fak1 = fbk
        fbk1 = f(xbk1)
        xw = 0.5*(xak1 + xUk1)
    else:
        xLk1 = xLk
        xUk1 = xbk
        xak1 = xUk1 - Ik2
        xbk1 = xak
        fbk1 = fak
        fak1 = f(xak1)
        xw = 0.5*(xLk1 + xbk1)

    xLk = xLk1
    xUk = xUk1
    xak = xak1
    xbk = xbk1
    fak = fak1
    fbk = fbk1
    Ik1 = Ik2
    i = i + 1

print('Minimum point:')
xs = xw
print('Minimum value of objective function:')
fs = f(xw)
print('Number of iterations performed:')
i
