from card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.deck = []
        for shape in ['♥', '♦', '♣', '♠']:
            for value in range(1, 14):
                self.deck.append(Card(shape, value))
        self.deck.append(Card(True))
        self.deck.append(Card(False))
        self.shuffle_deck()
        
    def get_deck(self) -> list:
        return self.deck
    
    def shuffle_deck(self) -> None:
        random.shuffle(self.deck)

    def draw_cards(self, num: int) -> list:
        cards = []
        for _ in range(num):
            cards.append(self.deck.pop())
        return cards

    def throw_cards(self, num: int) -> bool:
        if num > 5 or num < 1 or num > len(self.deck):
            return False
        for _ in range(num):
            self.deck.pop()
        return True
    