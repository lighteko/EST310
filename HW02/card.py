class Card:
    # initializer for the regular cards
    def __init__(self, shape: str, value: int) -> None:
        if shape == 'hearts' or shape == 'diamonds':
            self.color = True
        else:
            self.color = False
        self.value = value
        self.shape = shape
    
    # initializer for the joker card
    def __init__(self, color: bool) -> None:
        self.color = color
        self.value = 0
        self.shape = 'joker'
        
    def get_shape(self) -> str:
        return self.shape
    
    def get_value(self) -> int:
        return self.value
    
    def get_color(self) -> bool:
        return self.color
