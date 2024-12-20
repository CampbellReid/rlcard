'''
    Original file name: bridge/player.py
    Original Author: William Hale
    Date created: 11/25/2021
    
    File name: five_hundred/player.py
    Modified by: Campbell Reid
    Date modified: 2024-11-06
'''

from typing import List

from .utils.five_hundred_card import FiveHundredCard


class FiveHundredPlayer:

    def __init__(self, player_id: int, np_random):
        ''' Initialize a BridgePlayer player class

        Args:
            player_id (int): id for the player
        '''
        if player_id < 0 or player_id > 3:
            raise Exception(f'BridgePlayer has invalid player_id: {player_id}')
        self.np_random = np_random
        self.player_id: int = player_id
        self.hand: List[FiveHundredCard] = []

    def remove_card_from_hand(self, card: FiveHundredCard):
        self.hand.remove(card)

    def __str__(self):
        return ['N', 'E', 'S', 'W'][self.player_id]
