# Arquivo de testes

import numpy as np
import RobPy as rp

a = rp.cria_vetor3([1, 2, 3])
b = rp.cria_vetor3([4, 5, 6])

print(a)
print(type(a))
print(a.shape)

print(rp.produto_escalar(a, b))

print(rp.norma_vetor(a))
