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

a_b = rp.proj_vetores(a, b)
print(a_b)
print(rp.norma_vetor(a_b))
print(rp.tamanho_proj_vetores(a, b))

print(rp.produto_vetorial(a, b))
