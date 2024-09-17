class Card:
    def __init__(self, shape: str, value: int) -> None:
        self.value = value
        self.shape = shape
        
    def get_shape(self) -> str:
        return self.shape
    
    def get_value(self) -> str:
        value = self.value
        if value == 1:
            value = 'A'
        elif value == 11:
            value = 'J'
        elif value == 12:
            value = 'Q'
        elif value == 13:
            value = 'K'
        return str(value)
    