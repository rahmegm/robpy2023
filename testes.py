# Arquivo de testes

import numpy as np
import RobPy as rp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# a = rp.cria_vetor3([1, 2, 3])
# b = rp.cria_vetor3([4, 5, 6])
#
# print(a)
# print(type(a))
# print(a.shape)
#
# print(rp.produto_escalar(a, b))
#
# print(rp.norma_vetor(a))
#
# a_b = rp.proj_vetores(a, b)
# print(a_b)
# print(rp.norma_vetor(a_b))
# print(rp.tamanho_proj_vetores(a, b))
#
# print(rp.produto_vetorial(a, b))

# PLOTAR VETORES
# a = rp.cria_vetor3([1, 2, 3])
# b = rp.cria_vetor3([1, 2, 1])
#
# fig: plt.Figure = plt.figure()
# ax = Axes3D(fig)
# fig.add_axes(ax)
# rp.plota_vetor3(a, color='r')
# rp.plota_vetor3(b, vo=a)
# plt.xlabel('Eixo X')
# plt.ylabel('Eixo Y')
# ax.set_zlabel('Eixo Z')
# plt.show()

# MATRIZ ROTAÇÃO
# print(rp.matriz_rotacao_x(60))
# print()
# print(np.cos(60))
# print(np.sin(60))
# print()
# print(rp.matriz_rotacao_y(60))
# print()
# print(rp.matriz_rotacao_z(60))

# print(rp.cria_vetor4(a))

# R = rp.matriz_rotacao_x(43*np.pi/180)
# r = rp.cria_vetor3([2, 3, 1])
#
# T = rp.cria_operador4(m_rot_b_a=R, v_o_a=r)
#
# print(T)
# print(np.linalg.inv(T))
