import sys
sys.path.append("../../")
from sqare_paint import Player, Option ,Field


option = Option()

def test_option():
    assert option.width==5
    assert option.height==5
    assert option.num_players==4

def test_player():
    player = Player(0, option)
    assert player.id == 0
    assert (player.pos_x, player.pos_y) == (1, 1)

def test_field():
    field = Field(option)
    assert len(field.field) == option.height+2