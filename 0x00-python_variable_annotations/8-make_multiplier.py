#!/usr/bin/env python3
'''Task 8
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns multiply func
    '''
    return lambda x: x * multiplier
