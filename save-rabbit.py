from functools import wraps

def memoized(f):
    """Decorator that caches a function's return value each time it is
    called. If called later with the same arguments, the cached value
    is returned, and not re-evaluated.

    """
    cache = {}
    @wraps(f)
    def wrapped(*args):
        try:
            result = cache[args]
        except KeyError:
            result = cache[args] = f(*args)
        return result
    return wrapped
    
def answer(food, grid):
    @memoized
    def r(t, i, j):
        # Smallest remainder from t after subtracting the numbers on a path
        # from top left to (i, j) in grid, or total + 1 if there is no
        # path whose sum is less than or equal to t.
        t -= grid[i][j]
        if i < 0 or j < 0 or t < 0:
            return food + 1
        elif i == j == 0:
            return t
        else:
            return min(r(t, i - 1, j), r(t, i, j - 1))

    remainder = r(food, len(grid) - 1, len(grid) - 1)
    return remainder if remainder <= food else -1
    
    
    
    
    
print answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
