class InvalidInputsError(Exception):

    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return (
            f'{repr(self.errors)} ')
