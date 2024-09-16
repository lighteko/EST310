class Card:
    # initializer for the regular cards
    def __init__(self, shape: str, value: int) -> None:
        if shape == '♥' or shape == '♦':
            self.color = True
        else:
            self.color = False
        self.value = value
        self.shape = shape
    
    # initializer for the joker card
    def __init__(self, color: bool) -> None:
        self.color = color
        self.value = 0
        self.shape = 'JOKER'
        
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
    
    def get_color(self) -> bool:
        return self.color
