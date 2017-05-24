#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Gabriel Cueto <TheMushr00m - @Mushr00m_Dev>


class matrix:
    _n = 0
    _m = 0
    _elems = None

    def __init__(self, n, m):
        """Inicializa la matriz con valor 0 en cada posición"""
        self._n = n
        self._m = m
        self._elems = []
        for i in range(self._n):
            self._elems.append([])
            for j in range(self._m):
                self._elems[i].append(0)

    def define_elem(self, i, j, v):
        """ Sobreescribe el valor de una celda """
        self._elems[i][j] = v

    def show_matrix(self):
        """ Imprime los valores almacenados en la matriz """
        for i in range(self._n):
            for j in range(self._m):
                # Imprime de una forma elegante la matriz
                print("| {0} ".format(self._elems[i][j]), sep=',', end='')
            print('|\n')

    def get_cols(self):
        """ Devuelve el número de columnas en la matriz """
        return self._m

    def get_rows(self):
        """ Devuelve el número de filas en la matriz """
        return self._n

    cols = property(fget=get_cols)
    rows = property(fget=get_rows)


m = matrix(3, 3)
m.show_matrix()
