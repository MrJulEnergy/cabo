import numpy as np

class PlayingCard:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.visible: bool = False
        
        if value == 7 or value == 8:
            self.special = "peek"

        elif value == 9 or value == 10:
            self.special = "spy"

        elif value == 11 or value == 12:
            self.special = "swap"
        
        else:
            self.special = None

class Deck:
    def __init__(self, cards: np.array(PlayingCard)) -> None:
        self.cards: np.array(PlayingCard) = cards
    
    def shuffle(self):
        np.random.shuffle(self.cards)
    
    def give(self, num: int) -> np.array(PlayingCard):
        # take cards from top (last elements in array)
        removed_cards = self.cards[-num:]
        self.cards = self.cards[:-num]
        return removed_cards


    def standard_set() -> np.array(PlayingCard):
        needed_cards = 2 * [0] + 4 * [num for num in range(1, 13)] + 2 * [13]
        card_set = np.array([PlayingCard(val) for val in needed_cards])
        return card_set
