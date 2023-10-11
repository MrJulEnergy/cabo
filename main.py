from __future__ import annotations
import numpy as np
from cards import PlayingCard, Deck

# Cabo Game



class Player:
    def __init__(self, starting_hand) -> None:
        self.hand = starting_hand

    def take(self, other: Deck):
        pass

    def swap(self, other: Player):
        pass

    def spy(self, other: Player):
        pass

    def peek(self):
        pass


class Game:
    def __init__(self, n_players: int, n_cards: int = 4) -> None:
        self.n_players: int = n_players # number of players
        self.n_cards: int = n_cards # number of cards each player starts with

        self.startup()
        self.game_loop()

    def startup(self):
        self.deck = Deck(Deck.standard_set())
        self.deck.shuffle()
        self.players = np.array([Player(self.deck.give(self.n_cards)) for _ in range(self.n_players)])

    def game_loop(self):
        #TODO
        pass

if __name__ == "__main__":
    g = Game(2)
    for player in g.players:
        for card in player.hand:
            print(card.value)