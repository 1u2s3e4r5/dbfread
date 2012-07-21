# -*- coding: utf-8 -*-

__author__ = 'Ole Martin Bjørndalen'
__email__ = 'ombdalen@gmail.com'
__url__ = 'http://nerdly.info/ole/'
__license__ = 'MIT'
__version__ = '0.1.0'

from .dbf import DBF as read

class RowObject(object):
    def __init__(self, items):
        self.__dict__.update(items)

__all__ = ['objfactory', 'read']
