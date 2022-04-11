import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from square_paint import *


option = Option()


def test_option():
    assert option.width == 5
    assert option.height == 5
    assert option.num_players == 4


def test_player():
    player = Player(0, option)
    assert player.id == 0
    assert (player.pos_x, player.pos_y) == (0, 0)


def test_field():
    field = Field(option)
    assert len(field.field) == option.height + 2


def test_simulator():
    assert start() != None
