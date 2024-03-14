#!/usr/bin/env python3
'''0x00. Python - Variable Annotations'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''calculate element length'''
    return [(i, len(i)) for i in lst]
