import time
import numpy as n
def conometro(func):
    def wrapper(*args, **kwargs):
        comeco = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        tempo = fim - comeco
        print(tempo)
        return resultado
    return wrapper

@njit
def minha_funcao():
    for i in range(1000000):
        print(i)

if __name__ == "__main__":
    minha_funcao_decorada = conometro(minha_funcao)
    minha_funcao_decorada()
