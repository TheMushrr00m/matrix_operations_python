#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Gabriel Cueto <TheMushr00m - @Mushr00m_Dev>


class Matrix:
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
                print("| {0} ".format(self.get_value_of_position(i, j)), sep=',', end='')
            print('|\n')

    def get_cols(self):
        """ Devuelve el número de columnas en la matriz """
        return self._m

    def get_rows(self):
        """ Devuelve el número de filas en la matriz """
        return self._n

    def get_value_of_position(self, i, j):
        """ Devuelve el valor en la fila(i), columna(j) de la matriz """
        return self._elems[i][j]

    def add(self, *matrix):
        """ Puede recibir varias matrices como argumentos """
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                tmp = self.get_value_of_position(i, j)
                for m in matrix:
                    tmp += m.get_value_of_position(i, j)
                row.append(tmp)
            yield row

    def scalar_product(self, x):
        """ x: Número real """
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.get_value_of_position(i, j)*x)
            yield row

    def product(self, m):
        """ Recibe una matriz como argumento
         Args:
             m (Matrix): Represents an instance of Matrix
        """
        if self.rows is not m.cols:
            raise Exception('Number of rows'
                            'and number of columns'
                            "don't match")
        for i in range(self.rows):
            row = []
            for j in range(m.cols):
                add = 0
                for c in range(self.cols):
                    add += self.get_value_of_position(i, c) * \
                           m.get_value_of_position(c, j)
                row.append(add)
            yield row

    def transpose(self):
        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.get_value_of_position(i,j))
            yield row

    cols = property(fget=get_cols)
    rows = property(fget=get_rows)