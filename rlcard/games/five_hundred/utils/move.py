'''
    Original file name: bridge/utils/move.py
    Original Author: William Hale
    Date created: 11/25/2021
    
    File name: five_hundred/utils/move.py
    Modified by: Campbell Reid
    Date modified: 2024-11-06
'''

#
#   These classes are used to keep a move_sheet history of the moves in a round.
#

from .action_event import ActionEvent, BidAction, PassAction, DblAction, RdblAction, PlayCardAction
from .five_hundred_card import FiveHundredCard

from ..player import FiveHundredPlayer


class FiveHundredMove(object):  # Interface
    pass


class PlayerMove(FiveHundredMove):  # Interface

    def __init__(self, player: FiveHundredPlayer, action: ActionEvent):
        super().__init__()
        self.player = player
        self.action = action


class CallMove(PlayerMove):  # Interface

    def __init__(self, player: FiveHundredPlayer, action: ActionEvent):
        super().__init__(player=player, action=action)


class DealHandMove(FiveHundredMove):

    def __init__(self, dealer: FiveHundredPlayer, shuffled_deck: [FiveHundredCard]):
        super().__init__()
        self.dealer = dealer
        self.shuffled_deck = shuffled_deck

    def __str__(self):
        shuffled_deck_text = " ".join([str(card) for card in self.shuffled_deck])
        return f'{self.dealer} deal shuffled_deck=[{shuffled_deck_text}]'


class MakePassMove(CallMove):

    def __init__(self, player: FiveHundredPlayer):
        super().__init__(player=player, action=PassAction())

    def __str__(self):
        return f'{self.player} {self.action}'


class MakeDblMove(CallMove):

    def __init__(self, player: FiveHundredPlayer):
        super().__init__(player=player, action=DblAction())

    def __str__(self):
        return f'{self.player} {self.action}'


class MakeRdblMove(CallMove):

    def __init__(self, player: FiveHundredPlayer):
        super().__init__(player=player, action=RdblAction())

    def __str__(self):
        return f'{self.player} {self.action}'


class MakeBidMove(CallMove):

    def __init__(self, player: FiveHundredPlayer, bid_action: BidAction):
        super().__init__(player=player, action=bid_action)
        self.action = bid_action  # Note: keep type as BidAction rather than ActionEvent

    def __str__(self):
        return f'{self.player} bids {self.action}'


class PlayCardMove(PlayerMove):

    def __init__(self, player: FiveHundredPlayer, action: PlayCardAction):
        super().__init__(player=player, action=action)
        self.action = action  # Note: keep type as PlayCardAction rather than ActionEvent

    @property
    def card(self):
        return self.action.card

    def __str__(self):
        return f'{self.player} plays {self.action}'
