import ctypes as ct



class CommonVar[VarType]:
    def __init__(self, value: VarType):
        setattr(self, '', value)

    def __assign__(self, value, permission):
        cls = self.get().__class__.__name__ 
        if permission not in cls or not isinstance(value, cls): raise ValueError
        setattr(self, '', value)
        return set(self.get())
    
    def __str__(self):
        return str(getattr(self, ''))
    
    def __call__(self, *args, **kwargs) -> str:
        return self.get()(*args, **kwargs)
    
    def __len__(self) -> int:
        return len(self.get())
    
    def __getitem__(self, item):
        return self.get()[item]

    def __setitem__(self, key, value):
        self.get().__setitem__(key, value)

    def get(self) -> VarType: getattr(self, '')

