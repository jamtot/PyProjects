from nose.tools import *
from game.game import Game

def test_game():
    mapx = 20
    mapy = 20
    testgame = Game(30, 30, 30, 30, mapx, mapy)
    assert_equal(testgame.map.get_size_x(), mapx)
    assert_equal(testgame.map.get_size_y(), mapy)

def test_populate():
    zombies = 30
    victims = 29
    hunters = 33
    testgame = Game(zombies, victims, hunters, 1, 20, 20)
    testgame.populate()

    zomb_count, vic_count, hunt_count = 0, 0, 0
    tile_list = testgame.get_map().get_list()
    for list in tile_list:
        for tile in list:
            if tile.get_occupier() == "Zombie":
                zomb_count+=1
            elif tile.get_occupier() == "Victim":
                vic_count+=1
            elif tile.get_occupier() == "Hunter":
                hunt_count+=1

    assert_equal(zomb_count, zombies)
    assert_equal(vic_count, victims)
    assert_equal(hunt_count, hunters)
