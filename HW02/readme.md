# [EST 310] Lose with the Joker
## Objective:
You need to reach a score of 100 or throw two Jokers to win.

# Rules:
1. On each turn, you can draw or throw cards from deck.
2. When you draw the cards, non-number cards have different effects:
   
**[Jokers]**: subtract *[(number of Jokers + number of Jacks) * number of cards]* from your score.
              If you have two Jokers in your hand, you lose.
              If you have a Joker but do not have a Jack, you get [2 * number of cards] points off.
              
**[Jacks]**:  subtract *[number of cards in your hand]* from your score.
              
**[Kings]**:  append *[2 * (number of Kings) * number of cards]* points.
              If you have 5 or more kings, you win. 
              
**[Queens]**: 2 Queens give you 1 King.
              
**[Aces]**:   Aces protect you from Jokers and Jacks. If you have at least one Ace in your hand, you get *[0.5 * number of cards]* points.
              If you have four Aces and you also have a Joker or Jacks, you get *[4 * number of cards]* points.

## There are special rules:
1.  If you have Jokers or Jacks and Kings in your hand at the same time, Kings cannot effect.
2.  Scores cannot be negative. If the score is negative, it is set to 0.
3.  You can throw cards at most 5 cards per turn, but you cannot throw more than the number of leftover cards in the deck.
4.  You can draw at most 15 cards per turn, but you cannot draw more than the number of leftover cards in the deck.
5.  You must draw after throwing cards.
6.  If you throw away two Jokers, you win.
7.  If you are run out of cards in the deck and you have not reached 100 points, you lose.
8.  If you don't have any non-number cards in your hand, you get [number of cards] points.
9.  If you have non-number cards in your hand but they are not affective, you get [number of cards] points.

Game made by Heejoon Yi, inspired from the original card game Lose with the Joker.
