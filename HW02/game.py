from deck import Deck

class Game:
    def __init__(self) -> None:
        self.score = 0
        self.deck = Deck()
        self.hand = []
        self.stopper = False

    def run(self) -> None:
        while not self.stopper:
            self.turn()
            self.score += self.evaluate_hand()
            self.print_score()
            self.print_num_cards()
            if self.check_win():
                break
        print("Game over.")
        if (input("Do you want to play again? [Y/N]: ").upper() == 'Y'):
            self.__init__()
            self.run()
        else:
            print("Thank you for playing!")

    def deal(self) -> None:
        num = int(input("Enter the number of cards you want to draw: "))
        cards = self.deck.draw_cards(num)
        self.hand = cards

    def throw(self) -> None:
        num = int(input("Enter the number of cards you want to throw: "))
        if self.deck.throw_cards(num):
            print("Cards thrown successfully.")
        else:
            print("Invalid number of cards to throw.")
            self.throw()

    def print_hand(self) -> None:
        print("Your hand: ", end='')
        print(" [", end='')
        for i, card in enumerate(self.hand):
            shape = card.get_shape()
            value = card.get_value()
            if shape == 'JOKER':
                print("JOKER", end='')
            else:
                print(shape + value, end='')
            if i != len(self.hand) - 1:
                print(", ", end='')
            else:
                print("]")

    def turn(self) -> None:
        choice = input("Choose to draw or throw [D/T]: ").upper()
        if choice == 'D':
            self.deal()
            self.print_hand()
        elif choice == 'T':
            self.throw()
        else:
            print("Invalid choice. Please try again.")
            self.turn()

    def check_win(self) -> bool:
        if (self.score >= 100):
            print("You win!")
            print(f"Your final score is: {self.score}")
            return True
        elif (len(self.deck.get_deck()) == 0):
            print("You lose!")
            print(f"Your final score is: {self.score}")
            return True
        else:
            return False

    def evaluate_hand(self) -> int:
        hand = self.hand
        score = 0
        jokers = self.count_joker()
        aces = self.count_cards('ANY', 'A')
        jacks = self.count_cards('ANY', 'J')
        kings = self.count_cards('ANY', 'K')
        queens = self.count_cards('ANY', 'Q')
        if (queens == 2):
            kings += 1
        elif (queens == 4):
            kings += 2

        if (jokers > 0):
            if (aces == 4):
                if (self.score == 0):
                    score += 2 * 4 * len(hand)
                else:
                    score += 2 * self.score
            elif (aces > 0):
                score += 0.5 * len(hand)
            else:
                score -= len(hand) * (jokers + jacks)
        elif (jacks > 0):
            if (aces == 4):
                if (self.score == 0):
                    score += 2 * 4 * len(hand)
                else:
                    score += 2 * self.score
            elif (aces > 0):
                score += 0.5 * len(hand)
            else:
                score -= len(hand)
        elif (kings > 0):
            if (kings >= 3):
                if (aces == 4):
                    self.win()
                else:
                    score += 6 * len(hand)
            else:
                if (aces == 4):
                    score += (kings + aces)
                else:
                    score += len(hand) * kings
        else:
            score += len(hand)
        self.hand.clear()
        if (score + self.score < 0):
            score = -self.score
        return score

    def count_joker(self) -> int:
        counter = 0
        for card in self.hand:
            if (card.get_shape() == 'JOKER'):
                counter += 1
        return counter

    def count_cards(self, shape: str, value: str) -> int:
        counter = 0
        if (shape == 'ANY'):
            for card in self.hand:
                if (card.get_value() == value):
                    counter += 1
        else:
            for card in self.hand:
                if (card.get_shape() == shape and card.get_value() == value):
                    counter += 1
        return counter

    def print_score(self) -> None:
        print(f"Your current score is: {self.score}")

    def print_num_cards(self) -> None: 
        print(f"Number of cards in the deck: {len(self.deck.get_deck())}")

    def win(self) -> None:
        print("You win!")
        self.stopper = True
