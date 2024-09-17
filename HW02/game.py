from deck import Deck

class Game:
    def __init__(self) -> None:
        self.score = 0
        self.deck = Deck()
        self.hand = []
        self.stopper = False
        self.thrown = []
        self.threw = False

    def print_message(self) -> None:
        message = """
# [EST 310] Welcome to the game: Lose with the Joker
## Objective:
You need to reach a score of 100 or throw two Jokers to win.

# Rules:
0. The deck must be shuffled before starting the game.
1. On each turn, you can draw or throw cards from the deck.
2. When you draw the cards, non-number cards have different effects:
   
[Jokers]: subtract [(number of Jokers + number of Jacks) * number of cards] from your score.
              If you have two Jokers in your hand, you lose.
              If you have a Joker but do not have a Jack, you get [2 * number of cards] points off.
              
[Jacks]:  subtract [number of cards in your hand] from your score.
              
[Kings]:  append [2 * (number of Kings) * number of cards] points.
              If you have 5 or more kings, you win. 
              
[Queens]: 2 Queens give you 1 King.
              
[Aces]:   Aces protect you from Jokers and Jacks. If you have at least one Ace in your hand, you get [0.5 * number of cards] points.
              If you have four Aces and you also have a Joker or Jacks, you get [4 * number of cards] points.

## There are special rules:
1.  If you have Jokers or Jacks and Kings in your hand at the same time, Kings cannot affect.
2.  Scores cannot be negative. If the score is negative, it is set to 0.
3.  You can throw at most 5 cards per turn, but you cannot throw more than the number of leftover cards in the deck.
4.  You can draw at most 15 cards per turn, but you cannot draw more than the number of leftover cards in the deck.
5.  You must draw after throwing cards.
6.  If you throw away two Jokers, you win.
7.  If you are run out of cards in the deck and you have not reached 100 points, you lose.
8.  If you don't have any non-number cards in your hand, you get [number of cards] points.
9.  If you have non-number cards in your hand but they are not effective, you get [number of cards] points.

Game made by Heejoon Yi, inspired from the original card game Lose with the Joker.

"""
        print(message)

    def run(self) -> None:
        self.print_message()

        while not self.stopper:
            self.turn()
            self.score += self.eval_hand()
            self.print_score()
            self.print_num_cards()
            if self.eval():
                break
        print("Game over.")
        if (input("Do you want to play again? [Y/N]: ").upper() == 'Y'):
            self.__init__()
            self.run()
            return
        else:
            print("Thank you for playing!")

    def deal(self) -> None:
        prompt = input("Enter the number of cards you want to draw: ")
        if not prompt.isdigit():
            print("Invalid input. Please enter a number.")
            self.deal()
            return
        num = int(prompt)
        if num == 0:
            print("You must draw at least one card.")
            self.deal()
            return
        elif num > 15:
            print("You can draw at most 15 cards per turn.")
            self.deal()
            return
        elif num > len(self.deck.get_deck()):
            print("There are not enough cards in the deck.")
            self.deal()
            return
        cards = self.deck.draw_cards(num)
        self.hand = cards
        self.threw = False

    def throw(self) -> None:
        prompt = input("Enter the number of cards you want to throw: ")
        if not prompt.isdigit():
            print("Invalid input. Please enter a number.")
            self.throw()
            return
        num = int(prompt)
        if num == 0:
            print("You must throw at least one card.")
            self.throw()
            return
        if num > 5:
            print("You can throw at most 5 cards per turn.")
            self.throw()
            return
        elif num > len(self.deck.get_deck()):
            print("You cannot throw more cards than you have in your deck.")
            self.throw()
            return
        cards = self.deck.throw_cards(num)
        self.thrown.extend(cards)
        self.threw = True

    def print_hand(self) -> None:
        print("Your hand: [", end='')
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

    def print_thrown(self) -> None:
        print("Thrown: [", end='')
        for i, card in enumerate(self.thrown):
            shape = card.get_shape()
            value = card.get_value()
            if shape == 'JOKER':
                print("JOKER", end='')
            else:
                print(shape + value, end='')
            if i != len(self.thrown) - 1:
                print(", ", end='')
            else:
                print("]")
    
    def turn(self) -> None:
        choice = input("Choose to draw or throw [D/T]: ").upper()
        if choice == 'D':
            self.deal()
            self.print_hand()
        elif choice == 'T':
            if self.threw:
                print("You must draw after throwing cards.")
                self.turn()
                return
            self.throw()
            self.print_thrown()
        else:
            print("Invalid choice. Please try again.")
            self.turn()

    def eval(self) -> bool:
        if (self.score >= 100):
            print("You win!")
            print(f"Your final score is: {self.score}")
            return True
        elif (len(self.deck.get_deck()) == 0):
            print("You lose!")
            print(f"Your final score is: {self.score}")
            return True
        elif (self.eval_thrown()):
            print("You win!")
            print(f"Your final score is: {self.score}")
            return True
        else:
            return False

    def eval_hand(self) -> int:
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

        if jokers == 2:
            self.lose()
            return 0
        elif jokers == 1 and aces  == 0:
            if jacks == 0:
                score -= 2 * len(hand)
            else:
                score -= (jokers + jacks) * len(hand)
        elif jokers == 1 and aces > 0 or jacks > 0 and aces > 0:
            if aces == 4:
                score += 4 * len(hand)
            else:
                score += 0.5 * len(hand)
        elif jacks > 0 and aces == 0:
            score -= len(hand)
        elif kings >= 5:
            self.win()
            return 0
        elif kings > 0:
            score += 2 * kings * len(hand)
        else:
            score += len(hand)
            
        if (score + self.score < 0):
            score = -self.score

        self.hand = []
        return score

    def eval_thrown(self) -> bool:
        jokers = 0
        for card in self.thrown:
            if (card.get_shape() == 'JOKER'):
                jokers += 1
        if (jokers == 2):
            return True
        return False
   
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
    
    def lose(self) -> None:
        print("You lose!")
        self.stopper = True
