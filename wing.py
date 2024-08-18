OO = float("infinity")

class Wing:
    """
    a container without order,
    you can get an object only with its id, allowing more security
    should not be modifed
    """
    _range = (2, -36)

    def __init__(self, limit=OO) -> None:
        setattr(self, '*', limit)
        setattr(self, ',', 0)

    def _(self, attr_name):
        return getattr(self, attr_name)
    
    def _i(self):
        setattr(self, ',', self._(',') + 1)
    
    def _d(self):
        setattr(self, ',', self._(',') - 1)

    def add(self, __object):
        if self._(',') >= self._('*'): return
        id_ = id(__object)
        setattr(self, str(id_), __object)
        self._i()
        return id_

    def remove(self, id: int|str):
        if not hasattr(self, str(id)):
            return
        obj = getattr(self, str(id))
        delattr(self, str(id))
        self._d()
        return obj
    
    def generate(self):
        for id in dir(self)[Wing._range[0]: Wing._range[1]]:
            yield self.get(id)
    
    def get(self, id: int|str, default=None):
        if default is None: return getattr(self, str(id))
        return getattr(self, str(id), default)

    def clear(self):
        L = dir(self)[Wing._range[0]: Wing._range[1]]
        for id_ in L:
            self.remove(id_)









