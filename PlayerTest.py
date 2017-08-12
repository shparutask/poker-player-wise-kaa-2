import json
import unittest

from player import Player


class TestStringMethods(unittest.TestCase):

    # def test_diff_rank(self):
    #     self.assertEqual(Player.betRequest(self, json.loads('{  "game_id": "598eb80f831444000400001c",  "big_blind": 30,  "bet_index": 7,  "minimum_raise": 985,  "small_blind": 15,  "players": [    {      "id": 0,      "bet": 1015,      "version": "Maverik",      "status": "active",      "name": "Maverik",      "time_used": 631148,      "stack": 1677    },    {      "id": 1,      "bet": 0,      "version": "0.1",      "status": "out",      "name": "Z team",      "time_used": 19945,      "stack": 0    },    {      "id": 2,      "bet": 0,      "version": "Default Java folding player",      "status": "out",      "name": "Excited Bird",      "time_used": 44940,      "stack": 0    },    {      "id": 3,      "bet": 30,      "hole_cards": [        {          "suit": "hearts",          "rank": "3"        },        {          "suit": "clubs",          "rank": "9"        }      ],      "version": "Default Python folding player",      "status": "active",      "name": "Wise Kaa 2",      "time_used": 702002,      "stack": 278    }  ],  "current_buy_in": 1015,  "orbits": 10,  "community_cards": [],  "tournament_id": "598e25d6b0cdd800040018da",  "pot": 1045,  "in_action": 3,  "dealer": 3,  "round": 40}')), 0)
    #
    def test_equals_rank(self):
        player = Player()
        self.assertEqual(player.betRequest(json.loads('{"in_action": 3, "tournament_id": "598e25d6b0cdd800040018da", "players": [{"status": "out", "name": "Maverik", "id": 0, "version": "Maverik", "time_used": 43696, "bet": 0, "stack": 0}, {"status": "active", "name": "Z team", "id": 1, "version": "0.1", "time_used": 2408637, "bet": 140, "stack": 3218}, {"status": "out", "name": "Excited Bird", "id": 2, "version": "Excited Fish", "time_used": 62689, "bet": 0, "stack": 0}, {"hole_cards": [{"rank": "A", "suit": "diamonds"}, {"rank": "8", "suit": "hearts"}], "status": "active", "name": "Wise Kaa 2", "id": 3, "version": "Default Python folding player", "time_used": 1972094, "bet": 140, "stack": 502}], "pot": 280, "dealer": 3, "orbits": 23, "bet_index": 2, "minimum_raise": 140, "small_blind": 70, "round": 93, "big_blind": 140, "community_cards": [{"rank": "10", "suit": "diamonds"}, {"rank": "5", "suit": "diamonds"}, {"rank": "6", "suit": "clubs"}], "game_id": "598ecf438314440004000096", "current_buy_in": 140}')), 0)

    # def dummy(self):
    #     self.assertEquals(1,1)

    def test_request(self):
        # raise NameError(res)
        player = Player()
        self.assertEqual(0, player.rank_request(json.loads('[{"suit": "hearts","rank": "3"},{"suit": "clubs","rank": "9"},{"rank": "10", "suit": "diamonds"}, {"rank": "5", "suit": "diamonds"}, {"rank": "6", "suit": "clubs"}]')))


    def test_all_cards(self):
        player = Player()
        self.assertEqual(5, len(player.getAllCards(json.loads('{"in_action": 3, "tournament_id": "598e25d6b0cdd800040018da", "players": [{"status": "out", "name": "Maverik", "id": 0, "version": "Maverik", "time_used": 43696, "bet": 0, "stack": 0}, {"status": "active", "name": "Z team", "id": 1, "version": "0.1", "time_used": 2408637, "bet": 140, "stack": 3218}, {"status": "out", "name": "Excited Bird", "id": 2, "version": "Excited Fish", "time_used": 62689, "bet": 0, "stack": 0}, {"hole_cards": [{"rank": "A", "suit": "diamonds"}, {"rank": "8", "suit": "hearts"}], "status": "active", "name": "Wise Kaa 2", "id": 3, "version": "Default Python folding player", "time_used": 1972094, "bet": 140, "stack": 502}], "pot": 280, "dealer": 3, "orbits": 23, "bet_index": 2, "minimum_raise": 140, "small_blind": 70, "round": 93, "big_blind": 140, "community_cards": [{"rank": "10", "suit": "diamonds"}, {"rank": "5", "suit": "diamonds"}, {"rank": "6", "suit": "clubs"}], "game_id": "598ecf438314440004000096", "current_buy_in": 140}'))))

if __name__ == '__main__':
    unittest.main()