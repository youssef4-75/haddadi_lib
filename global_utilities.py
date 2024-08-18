from numpy import exp as e, cos, sin


def absl(n, x_or_y, *, BX, BY, HEIGHT, WIDTH):
    if x_or_y: return int(BX * n / HEIGHT)
    return int(BY * n / WIDTH)


def ins_dicho(L, value, start = 0, end = None):
    if end is None: end = len(L) + 1
    n = end - start - 1
    if n == 0: L.insert(end, value); return
    if L[start + n//2][0] > value[0]: ins_dicho(L, value, start, start + n//2)
    elif L[start + n//2][0] < value[0]: ins_dicho(L, value, start + n//2 + 1, end)
    else: L.insert(start + n//2, value)

def my_range(start, end, step=1):
    if step > 0: val = lambda start: start < end
    elif step < 0: val = lambda start: start > end
    else: raise ValueError('Step must be non-zero') 
    while val(start):
        yield start
        start += step

def add_element(iterable, index, *value):
    try:
        iterable[index] += [[value]]
    except (IndexError, KeyError):
        try:
            iterable[index] = [[value]]
        except IndexError:
            iterable.append(value)


def exp(z:complex):
    return e(z.real) * complex(cos(z.imag), sin(z.imag))
