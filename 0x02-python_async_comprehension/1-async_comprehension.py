#!/usr/bin/env python3
'''Task 1
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Collect 10 random numbers using async comprehension over async_generator 
    then return them.
    '''
    return [num async for num in async_generator()]
