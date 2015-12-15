import numpy

class Card(object):
	"""Represents a standard playing card.
	
	Attributes:
	  suit: string
	  value: string
	"""

	def __init__(self, suit, value):
		self.value = value
		self.suit = suit

class Deck(object):
	"""Represents a standard playing deck.
	"""
	
	def __init__(self):
		self.cards = []
		suit_names = ['spades', 'hearts', 'diamonds', 'clovers']
		value_names =['1','2','3','4','5','6','7','8','9','jack','queen','king','ace']
		for i in suit_names:
			for j in value_names:
				card = Card(i, j))
				self.cards.append(card)

	def shuffle(self):
		numpy.random.shuffle(self.cards)

if __name__ == '__main__':
	deck = Deck()
	deck.shuffle()
