class Card:
    # initializer for the regular cards
    def __init__(self, shape: str, value: int):
        self.shape = shape
        self.value = value
    
    # initializer for the joker card
    def __init__(self, color: bool):
        self.color = color
        self.value = 0
        
    def get_shape(self):
        return self.shape
    
    def get_value(self):
        return self.value
