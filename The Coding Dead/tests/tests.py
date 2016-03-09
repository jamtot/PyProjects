from nose.tools import *
from game.game import Game

def test_game():
    mapx = 20
    mapy = 20
    testgame = Game(30, 30, 30, 30, mapx, mapy)
    assert_equal(testgame.map.get_size_x(), mapx)
    assert_equal(testgame.map.get_size_y(), mapy)
