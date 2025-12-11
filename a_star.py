# a_star.py

import heapq
from math import sqrt

def heuristic(a, b):
    """Simple heuristic: Euclidean distance between node labels if numeric.
       If not numeric, return 1 (fallback)."""
    try:
        return abs(int(a) - int(b))
    except:
        return 1  # Fallback heuristic for non-numeric labels