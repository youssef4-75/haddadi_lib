

class IncompatibleValueError(Exception):
    def __init__(self, given_type, excpected_type) -> None:
        super().__init__(f"Excpected an object of type {excpected_type\
        }, got {given_type} instead")