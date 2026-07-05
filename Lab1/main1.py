import random

print("""Rayaan Riyaz
         20691965
         rayaan.riyaz@icloud.com""")
print("""Course Policies:
         1. Assignments may be submitted up to 1 week late for a 15% penalty.
         2. Any student may request a regrade no later than 1 week after the assignment is returned.
         3. It is the student's responsibility to drop themselves from the course if they are no longer able to attend.""")

class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

class Deck:
  def __init__(self):
    self.cards = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    for suit in suits:
      for value in values:
        self.cards.append(Card(suit, value))
  def deal(self):
    if len(self.cards) == 0:
      return None
    return self.cards.pop()

  def shuffle(self):
      self.cards = []
      suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
      values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
      for suit in suits:
        for value in values:
          self.cards.append(Card(suit, value))
      random.shuffle(self.cards)
