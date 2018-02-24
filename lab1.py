# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:25:26 2018

@author: raveendra.swarna
"""


import itertools
import scipy
import scipy.optimize

A = np.array([
    [[1, 1], [3, 4], [6, 6], [6, 7]],
    [[1/4,1/3], [1, 1], [3, 4], [3, 4]],
    [[1/6, 1/6], [1/4, 1/3], [1, 1], [3, 4]],
    [[1/7,1/6], [1/4, 1/3], [1/4, 1/3], [1, 1]]
])
AL = A[:, :, 0]
AU = A[:, :, 1]

def fill_lower(r, a, k, i, j):
    r[k, j + a.shape[1]] = a[i, j]
    r[k, i] = -1

def fill_upper(r, a, k, i, j):
    r[k,  i + a.shape[0]] = 1
    r[k,  j] = -a[i, j]
        
def create_matrix(a, f):
    " w_1^L, ... w_n^L, w_1^U, ..., w_n^[l]"
    
    n, _ =  a.shape
    r = np.zeros((n * n, 2 * n))
    for k, p in enumerate(itertools.product(range(n), range(n))):
        f(r, a, k, p[0], p[1])
    return r
        
def solve_lower(l, u):
    m, n = l.shape
    assert(m == n)
    assert(l.shape == u.shape)
    a1 = create_matrix(l, fill_lower)
    a2 = create_matrix(u, fill_upper)
    a = np.concatenate([a1, a2])
    b = np.zeros(a.shape[0])
    c = np.zeros(n + n)
    c[0:n] = -1
    c[n:] = 1
    c = -c
    return scipy.optimize.linprog(c, a, b, bounds=[(1, 100) for i in range(n + n)])

x = solve_lower(AL, AU)
x.fun

x.x