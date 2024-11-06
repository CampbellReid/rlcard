'''
    Original file name: bridge/utils/utils.py
    Original Author: William Hale
    Date created: 11/26/2021
    
    File name: five_hundred/utils/utils.py
    Modified by: Campbell Reid
    Date modified: 2024-11-06
'''

from typing import List

import numpy as np

from .five_hundred_card import FiveHundredCard


def encode_cards(cards: List[FiveHundredCard]) -> np.ndarray:  # Note: not used ??
    plane = np.zeros(52, dtype=int)
    for card in cards:
        plane[card.card_id] = 1
    return plane
