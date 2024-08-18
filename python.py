

from typing import Any


class Python[H]:
    def __init__(self, *objects:H) -> None:
        self.__OBJ_TUPLE = objects

    def __call__(self, method, *args: Any, **kwds: Any) -> Any:
        if isinstance(method, str):
            def method_(obj, *args, **kwargs):
                a = getattr(obj, method)
                if callable(a): return a(*args, **kwargs)
                else: return a 
        elif callable(method): method_ = method
        else: print(type(method)); raise TypeError
        return Python(*[
            method_(obj, *args, **kwds) for obj in self.__OBJ_TUPLE
        ])
    
    def __len__(self):
        return len(self.__OBJ_TUPLE)
    
    def activate(self, Player, keys, EXISTENCE,
            time, id_set):
        state = 0
        mana = 0
        activity = 0
        if Player.not_active(): return mana, state, activity
        for Skill in self.__OBJ_TUPLE:
            if mana != 0: break
            mana_, state, activity = Skill.used(
                keys=keys, EXISTENCE=EXISTENCE,
                time=time, id_set=id_set
                    )
            mana += mana_
        return mana, state, activity

