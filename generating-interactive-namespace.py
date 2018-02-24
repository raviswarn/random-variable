# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:33:28 2018

@author: raveendra.swarna
"""
# Populating the interactive namespace from numpy and matplotlib

import numpy as np
import pandas as pd


def diff_equation(a=None, b=None, dy=None, du=None):
    return a.dot(dy) + b.dot(du)

def control_matrix(a=None, b=None):
    n = a.shape[0]
    matricies = [b]
    current_a = a
    for i in range(1, n):
        matricies.append(current_a.dot(b))
        current_a = current_a.dot(a)
    return np.concatenate(matricies, axis=1)


def generate_r(a, lambdas, b, p):
    n = len(lambdas)
    cols = []
    ones = np.ones(n)
    for j, l in enumerate(lambdas):
        inv = np.linalg.inv(a - l * np.diag(ones))
        z = inv.dot(b).dot(p[:, j])
        cols.append(z.reshape((n, 1)))
        
    return np.concatenate(cols, axis=1)

lambdas = np.array([0.25, 0.55, 0.3, 0.2, 0.1, 0.35, 0.7, 0.6])

A = np.array([
    [0.0, -0.2, -0.25, 0.0, 0.0, 0.0, 0.7, -0.15],
    [0.8, 0.8, -0.4, 0.0, 0.0, 0.4, 0.0, 0.0],
    [-0.6, 0.0, 0.0, 0.0, 0.0, 0.0, -0.3, 0.0],
    [0.2, 0.0, 0.8, 0.75, 0.0, 0.5, 0.0, -0.3],
    [0.0, 0.0, 0.0, 0.7, 0.0, 0.0, 0.0, 0.0],
    [-0.5, 0.0, -0.4, 0.0, 0.2, 0.8, 0.0, 0.7],
    [0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.65, -0.3],
    [-0.3, 0.0, -0.6, 0.0, 0.3, 0.0, 0.4, 0.0]
])

B = np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
])

P = np.array([
    [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    [1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
])

delta_y = np.random.random(A.shape[1])
delta_u = np.random.random(B.shape[1])
A_eigen_values, A_eigen_vectors = np.linalg.eig(A)
R = generate_r(A, lambdas, B, P)
K_p_dash = P.dot(np.linalg.inv(R))

pd.DataFrame(R)

pd.DataFrame(K_p_dash)

pd.DataFrame(data={'Values1': A_eigen_values, 'Value2': np.abs(A_eigen_values)})

Q_c = control_matrix(A, B)
Q_c_rank = np.linalg.matrix_rank(Q_c)
print("Rank = %d" % Q_c_rank)