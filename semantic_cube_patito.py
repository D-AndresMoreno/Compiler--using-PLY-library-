from ply import *
import numpy as np


semantic_cube = {
    'int': {
        'int': {
            '<': 'bool',
            '>': 'bool',
            '*': 'int',
            '+': 'int',
            '=': 'int',
            '/': 'float',
            '-': 'int',
            '!=': 'bool'
        },
        'float': {
            '<': 'bool',
            '>': 'bool',
            '*': 'float',
            '+': 'float',
            '=': 'error',
            '/': 'float',
            '-': 'float',
            '!=': 'bool'
        },
        'bool': {
            '<': 'error',
            '>': 'error',
            '*': 'error',
            '+': 'error',
            '=': 'error',
            '/': 'error',
            '-': 'error',
            '!=': 'error'
        }
    },
    'float': {
        'int': {
            '<': 'bool',
            '>': 'bool',
            '*': 'float',
            '+': 'float',
            '=': 'float',
            '/': 'float',
            '-': 'float',
            '!=': 'bool'
        },
        'float': {
            '<': 'bool',
            '>': 'bool',
            '*': 'float',
            '+': 'float',
            '=': 'float',
            '/': 'float',
            '-': 'float',
            '!=': 'bool'
        },
        'bool': {
            '<': 'error',
            '>': 'error',
            '*': 'error',
            '+': 'error',
            '=': 'error',
            '/': 'error',
            '-': 'error',
            '!=': 'error'
        }
    },
    'bool': {
        'int': {
            '<': 'error',
            '>': 'error',
            '*': 'error',
            '+': 'error',
            '=': 'error',
            '/': 'error',
            '-': 'error',
            '!=': 'error'
        },
        'float': {
            '<': 'error',
            '>': 'error',
            '*': 'error',
            '+': 'error',
            '=': 'error',
            '/': 'error',
            '-': 'error',
            '!=': 'error'
        },
        'bool': {
            '<': 'error',
            '>': 'error',
            '*': 'error',
            '+': 'error',
            '=': 'bool',
            '/': 'error',
            '-': 'error',
            '!=': 'bool'
        }
    }
}

print(np.matrix(semantic_cube))                