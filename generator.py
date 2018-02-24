# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:15:28 2018

@author: raveendra.swarna
"""
class Generator(object):
    def __init__(self, function, w0, *args):
        self.args = args
        self.storage = [w0]
        self.function = function

    def reserve(self, n):
        _ = self[n]

    def __getitem__(self, n):
        if type(n) == slice:
            self.reserve(n.stop)
            return self.storage[n]
        if n <= len(self.storage):
            return self.storage[n]
        minimum = len(self.storage)
        for i in range(minimum, n + 1):
            self.storage.append(self.function(self.storage[i - 1], *self.args))
        return self.storage[n]
